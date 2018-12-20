/**************************************************************************//**
 * @file     main.c
 * @version  V2.00
 * $Revision: 6 $
 * $Date: 15/01/16 11:44a $
 * @brief    Show how to set GPIO pin mode and use pin data input/output control.
 * @note
 * Copyright (C) 2014 Nuvoton Technology Corp. All rights reserved.
 ******************************************************************************/
#include <stdio.h>
#include "NUC131.h"

#define PLL_CLOCK   50000000
/*define cmd for uart*/
#define UP '1'
#define DOWN '2'
#define LEFT '3'
#define RIGHT '4'
#define OK '5'
#define CANCEL '6'
#define RUNG_YEU 'r'
#define RUNG_MANH 'R'


#define RXBUFSIZE   1024

uint8_t g_u8RecData[RXBUFSIZE]  = {0};

volatile uint32_t g_u32comRbytes = 0;
volatile uint32_t g_u32comRhead  = 0;
volatile uint32_t g_u32comRtail  = 0;


void SYS_Init(void)
{
    /*---------------------------------------------------------------------------------------------------------*/
    /* Init System Clock                                                                                       */
    /*---------------------------------------------------------------------------------------------------------*/

    /* Enable Internal RC clock */
    CLK_EnableXtalRC(CLK_PWRCON_OSC22M_EN_Msk);

    /* Waiting for IRC22M clock ready */
    CLK_WaitClockReady(CLK_CLKSTATUS_OSC22M_STB_Msk);

    /* Switch HCLK clock source to Internal RC and HCLK source divide 1 */
    CLK_SetHCLK(CLK_CLKSEL0_HCLK_S_HIRC, CLK_CLKDIV_HCLK(1));

    /* Enable external 12MHz XTAL, internal 22.1184MHz */
    CLK_EnableXtalRC(CLK_PWRCON_XTL12M_EN_Msk | CLK_PWRCON_OSC22M_EN_Msk);

    /* Enable PLL and Set PLL frequency */
    CLK_SetCoreClock(PLL_CLOCK);

    /* Waiting for clock ready */
    CLK_WaitClockReady(CLK_CLKSTATUS_PLL_STB_Msk | CLK_CLKSTATUS_XTL12M_STB_Msk | CLK_CLKSTATUS_OSC22M_STB_Msk);

    /* Switch HCLK clock source to PLL, STCLK to HCLK/2 */
    //CLK_SetHCLK(CLK_CLKSEL0_HCLK_S_PLL, CLK_CLKDIV_HCLK(2));
    CLK_SetHCLK(CLK_CLKSEL0_HCLK_S_HXT, CLK_CLKDIV_HCLK(1));

    /* Enable UART module clock */
    CLK_EnableModuleClock(UART0_MODULE);

    /* Enable PWM module clock */
    CLK_EnableModuleClock(PWM1_MODULE);

    /* Select UART module clock source */
    CLK_SetModuleClock(UART0_MODULE, CLK_CLKSEL1_UART_S_HXT, CLK_CLKDIV_UART(1));

    /* Select PWM module clock source */
    CLK_SetModuleClock(PWM1_MODULE, CLK_CLKSEL3_PWM1_S_PCLK, 0);

    /* Reset PWM0 and PWM1 */
    SYS_ResetModule(PWM1_RST);

    /* Update System Core Clock */
    /* User can use SystemCoreClockUpdate() to calculate PllClock, SystemCoreClock and CycylesPerUs automatically. */
    //SystemCoreClockUpdate();
    PllClock        = PLL_CLOCK;            // PLL
    SystemCoreClock = PLL_CLOCK / 1;        // HCLK
    CyclesPerUs     = PLL_CLOCK / 1000000;  // For SYS_SysTickDelay()

    /*---------------------------------------------------------------------------------------------------------*/
    /* Init I/O Multi-function                                                                                 */
    /*---------------------------------------------------------------------------------------------------------*/
    /* Set GPB multi-function pins for UART0 RXD and TXD */
    SYS->GPB_MFP &= ~(SYS_GPB_MFP_PB0_Msk | SYS_GPB_MFP_PB1_Msk);
    SYS->GPB_MFP |= (SYS_GPB_MFP_PB0_UART0_RXD | SYS_GPB_MFP_PB1_UART0_TXD);

    /* Set GPA multi-function PWM1 channel 0 */
    SYS->GPA_MFP &= ~(SYS_GPA_MFP_PA2_Msk);
    SYS->GPA_MFP |= SYS_GPA_MFP_PA2_PWM1_CH0;
    SYS->ALT_MFP3 &= ~(SYS_ALT_MFP3_PA2_Msk);
    SYS->ALT_MFP3 |= SYS_ALT_MFP3_PA2_PWM1_CH0;
}

void UART0_Init()
{
    /*---------------------------------------------------------------------------------------------------------*/
    /* Init UART                                                                                               */
    /*---------------------------------------------------------------------------------------------------------*/
    /* Reset UART0 module */
    SYS_ResetModule(UART0_RST);

    /* Configure UART0 and set UART0 Baudrate */
    UART_Open(UART0, 115200);
}

/*port and pin for button*/
#define PORT_UP PC
#define PORT_DOWN PC
#define PORT_LEFT PC
#define PORT_RIGHT PC
#define PORT_OK PB
#define PORT_CANCEL PA

#define PIN_UP PC8
#define PIN_DOWN PC11
#define PIN_LEFT PC0
#define PIN_RIGHT PC14
#define PIN_OK PB13
#define PIN_CANCEL PA11

#define BIT_UP BIT8
#define BIT_DOWN BIT11
#define BIT_LEFT BIT0
#define BIT_RIGHT BIT14
#define BIT_OK BIT13
#define BIT_CANCEL BIT11

/*gpio NUC and NODE*/
#define PORT_NUC_NODE PB
#define PIN_NUC_NODE PB6
#define BIT_NUC_NODE BIT6

void User_GPIO_Init(void){
	GPIO_SetMode(PORT_UP, BIT_UP, GPIO_PMD_INPUT);
  GPIO_SetMode(PORT_DOWN, BIT_UP, GPIO_PMD_INPUT);
  GPIO_SetMode(PORT_LEFT, BIT_UP, GPIO_PMD_INPUT);
  GPIO_SetMode(PORT_RIGHT, BIT_UP, GPIO_PMD_INPUT);
  GPIO_SetMode(PORT_OK, BIT_UP, GPIO_PMD_INPUT);
  GPIO_SetMode(PORT_CANCEL, BIT_UP, GPIO_PMD_INPUT);
}

void User_Delay(unsigned int s) {
	unsigned int i=0;
	while (s>=1) {
		for (i=0; i<=65000; i++) {}
		s--;
	}
}

/*---------------------------------------------------------------------------------------------------------*/
/* MAIN function                                                                                           */
/*---------------------------------------------------------------------------------------------------------*/
int main(void)
{
    int32_t i32Err;

    /* Unlock protected registers */
    SYS_UnlockReg();

    /* Init System, peripheral clock and multi-function I/O */
    SYS_Init();

    /* Lock protected registers */
    SYS_LockReg();

    /* Init UART0 for printf */
    UART0_Init();

		
    /* Configure gpio*/
    User_GPIO_Init();
		
		/* Enable Interrupt and install the call back function */
    UART_EnableInt(UART0, (UART_IER_RDA_IEN_Msk));
	
		/*--------------------------------------------------------------------------------------*/
    /* Set the PWM1 Channel 0 as PWM output function.                                       */
    /*--------------------------------------------------------------------------------------*/

    /* Assume PWM output frequency is 250Hz and duty ratio is 30%, user can calculate PWM settings by follows.
        duty ratio = (CMR+1)/(CNR+1)
        cycle time = CNR+1
        High level = CMR+1
        WM clock source frequency = __HXT = 12000000
				(CNR+1) = PWM clock source frequency/prescaler/clock source divider/PWM output frequency
                = 12000000/2/1/250 = 24000
        (Note: CNR is 16 bits, so if calculated value is larger than 65536, user should increase prescale value.)
        CNR = 23999
        duty ratio = 30% ==> (CMR+1)/(CNR+1) = 30%
        CMR = 7199
        Prescale value is 1 : prescaler= 2
        Clock divider is PWM_CSR_DIV1 : clock divider =1
    */

    /* set PWM1 channel 0 output configuration */
    PWM_ConfigOutputChannel(PWM1, 0, 250, 0);

    /* Enable PWM Output path for PWM1 channel 0 */
    PWM_EnableOutput(PWM1, PWM_CH_0_MASK);

    /* Enable Timer for PWM1 channel 0 */
    PWM_Start(PWM1, PWM_CH_0_MASK);

    while(1) {
			
			if (PIN_UP!=1) {
				while(PIN_UP!=1);
				printf("%c",UP);
				User_Delay(10);
				
			}
			if (PIN_DOWN!=1) {
				while(PIN_DOWN!=1);
				printf("%c",DOWN);
				User_Delay(10);
			}
			if (PIN_LEFT!=1) {
				while(PIN_LEFT!=1);
				printf("%c",LEFT);
				User_Delay(10);
			}
			if (PIN_RIGHT!=1) {
				while(PIN_RIGHT!=1);
				printf("%c",RIGHT);
				User_Delay(10);
			}
			if (PIN_OK!=1) {
				while(PIN_OK!=1);
				printf("%c",OK);
				User_Delay(10);
			}
			if (PIN_CANCEL!=1) {
				while(PIN_CANCEL!=1);
				printf("%c",CANCEL);
				User_Delay(10);
			}
			
		}
}

void UART02_IRQHandler(void)
{
		uint8_t u8InChar = 0xFF;
    uint32_t u32IntSts = UART0->ISR;

    if(u32IntSts & UART_ISR_RDA_INT_Msk)
    {
        /* Get all the input characters */
        while(UART_IS_RX_READY(UART0))
        {
            /* Get the character from UART Buffer */
            u8InChar = UART_READ(UART0);
						
						//handle inchar here
						if (u8InChar == RUNG_YEU) {
							PWM_ConfigOutputChannel(PWM1, 0, 250, 10); //kich hoat dong co rung
							User_Delay(8); //delay
							PWM_ConfigOutputChannel(PWM1, 0, 250, 0); //disable dong co rung
						}
						if (u8InChar == RUNG_MANH) {
							PWM_ConfigOutputChannel(PWM1, 0, 250, 100);
							User_Delay(20);
							PWM_ConfigOutputChannel(PWM1, 0, 250, 0);
						}
        }
    }

    
}

/*** (C) COPYRIGHT 2014 Nuvoton Technology Corp. ***/
