#game.py
#_...........khoi tao game va xu li lenh tu tay cam....................._

import database_banthuyen

#huong dat thuyen
horizontal = 1
vertical = 2

#trang thai choi
start = 0
picking = 1
play = 2

## x-> 1
## fire -> 2
## ship -> 3

class game:
    # Init 2 team
    team1 = []
    team2 = []

    def __init__(self):
        print('initializing')
        self.current_step = 1 #trang thai tro choi
        self.player1_picking = 1 #khoi thuyen dat
        self.player2_picking = 1
        self.currentPlayer = 1 #nguoi choi hien tai
        self.player1_x = 0 #vi tri cua player1
        self.player1_y = 0
        self.player1_dimension = horizontal #huong dat thuyen
        self.player2_x = 0
        self.player2_y = 0
        self.player2_dimension = horizontal
        
        self.player1_hit = 0 #so thuyen bi ban trung
        self.player2_hit = 0
        
        self.database = database_banthuyen.database()
        #update trang thai tro choi
        self.database.update_current_step(str(1))
        #update trang thai nguoi choi
        self.database.update_status_player(player='player1', value='playing', room=3)
        self.database.update_status_player(player='player2', value='playing', room=3)
        #tao 2 mang 2 chieu matrix cho 2 nguoi choi
        for i in range(0,10):
            self.team1.append([0,0,0,0,0,0,0,0,0,0])
            self.team2.append([0,0,0,0,0,0,0,0,0,0])
            
    def reset(self):
      self.current_step = 1
      self.player1_picking = 1
      self.player2_picking = 1
      self.currentPlayer = 1
      self.player1_x = 0
      self.player1_y = 0
      self.player1_dimension = horizontal
      self.player2_x = 0
      self.player2_y = 0
      self.player2_dimension = horizontal
      
      self.player1_hit = 0
      self.player2_hit = 0

      self.database.update_status_player(player='player1', value='playing', room=3)
      self.database.update_status_player(player='player2', value='playing', room=3)

      self.team1=[]
      self.team2=[]
      for i in range(0,10):
          self.team1.append([0,0,0,0,0,0,0,0,0,0])
          self.team2.append([0,0,0,0,0,0,0,0,0,0])
    
    #ham dat thuyen (dat 3 khoi thuyen, tong cong 6 thuyen)      
    def put_ship(self, id):
      print('putting ship')
      if not self.check_conflict(id): #kiem tra dieu kien dat thuyen
        print('conflict ship!')
        return 0
      else:
        if id == '1':
          print(self.player1_x, self.player1_y)
          if (self.player1_picking == 1): #ship 1
            self.team1[self.player1_x][self.player1_y] = 3
            self.database.update_status(str(self.player1_x * 10 + self.player1_y), 'SHIP')
            self.player1_picking = 2
            print('ship 1 setted')
          elif (self.player1_picking == 2): #ship 2
            self.player1_picking = 3
            if self.player1_dimension == vertical:
              self.team1[self.player1_x][self.player1_y] = 3
              self.team1[self.player1_x + 1][self.player1_y] = 3
              self.database.update_status(str(self.player1_x * 10 + self.player1_y), 'SHIP')
              self.database.update_status(str((self.player1_x + 1) * 10 + self.player1_y), 'SHIP')
            else:
              self.team1[self.player1_x][self.player1_y] = 3
              self.team1[self.player1_x][self.player1_y + 1] = 3
              self.database.update_status(str(self.player1_x * 10 + self.player1_y), 'SHIP')
              self.database.update_status(str(self.player1_x * 10 + (self.player1_y + 1)), 'SHIP')
          elif (self.player1_picking == 3): #ship 3
            self.player1_picking = 4
            if self.player1_dimension == vertical:
              self.team1[self.player1_x][self.player1_y] = 3
              self.team1[self.player1_x + 1][self.player1_y] = 3
              self.team1[self.player1_x + 2][self.player1_y] = 3
              self.database.update_status(str(self.player1_x * 10 + self.player1_y), 'SHIP')
              self.database.update_status(str((self.player1_x + 1) * 10 + self.player1_y), 'SHIP')
              self.database.update_status(str((self.player1_x + 2) * 10 + self.player1_y), 'SHIP')
            else:
              self.team1[self.player1_x][self.player1_y] = 3
              self.team1[self.player1_x][self.player1_y + 1] = 3
              self.team1[self.player1_x][self.player1_y + 2] = 3
              self.database.update_status(str(self.player1_x * 10 + self.player1_y), 'SHIP')
              self.database.update_status(str(self.player1_x * 10 + (self.player1_y + 1)), 'SHIP')
              self.database.update_status(str(self.player1_x * 10 + (self.player1_y + 2)), 'SHIP')
            
        
        elif id == '2':
          if (self.player2_picking == 1): #ship 1
            self.player2_picking = 2
            self.team2[self.player2_x][self.player2_y] = 3
            self.database.update_status(str(self.player2_x * 10 + self.player2_y + 100), 'SHIP')
          elif (self.player2_picking == 2): #ship 2
            self.player2_picking = 3
            if self.player2_dimension == vertical:
              self.team2[self.player2_x][self.player2_y] = 3
              self.team2[self.player2_x + 1][self.player2_y] = 3
              self.database.update_status(str(self.player2_x * 10 + self.player2_y + 100), 'SHIP')
              self.database.update_status(str((self.player2_x + 1) * 10 + self.player2_y + 100), 'SHIP')
            else:
              self.team2[self.player2_x][self.player2_y] = 3
              self.team2[self.player2_x][self.player2_y + 1] = 3
              self.database.update_status(str(self.player2_x * 10 + self.player2_y + 100), 'SHIP')
              self.database.update_status(str(self.player2_x * 10 + (self.player2_y + 1) + 100), 'SHIP')
          elif (self.player2_picking == 3): #ship 3
            self.player2_picking = 4
            if self.player2_dimension == vertical:
              self.team2[self.player2_x][self.player2_y] = 3
              self.team2[self.player2_x + 1][self.player2_y] = 3
              self.team2[self.player2_x + 2][self.player2_y] = 3
              self.database.update_status(str(self.player2_x * 10 + self.player2_y + 100), 'SHIP')
              self.database.update_status(str((self.player2_x + 1) * 10 + self.player2_y + 100), 'SHIP')
              self.database.update_status(str((self.player2_x + 2) * 10 + self.player2_y + 100), 'SHIP')
            else:
              self.team2[self.player2_x][self.player2_y] = 3
              self.team2[self.player2_x][self.player2_y + 1] = 3
              self.team2[self.player2_x][self.player2_y + 2] = 3
              self.database.update_status(str(self.player2_x * 10 + self.player2_y + 100), 'SHIP')
              self.database.update_status(str(self.player2_x * 10 + (self.player2_y + 1) + 100), 'SHIP')
              self.database.update_status(str( self.player2_x * 10 + (self.player2_y + 2) + 100), 'SHIP')
      if (self.player1_picking == 4 and self.player2_picking == 4):
        self.current_step = play
        self.database.update_current_step(str(2))
      return 1
    

    #ham nay se kiem tra tat ca cac o duoc dat thuyen xem co phai la o trong hay khong 
    def check_conflict(self, id):
      if id == '1':
          if (self.player1_picking == 1): #ship 1
              if self.team1[self.player1_x][self.player1_y] != 0:
                  return 0
          elif (self.player1_picking == 2): #ship 2
              if self.player1_dimension == vertical:
                  if self.team1[self.player1_x][self.player1_y] != 0:
                      return 0
                  if self.team1[self.player1_x + 1][self.player1_y] != 0:
                      return 0
              elif self.player1_dimension == horizontal:
                  if self.team1[self.player1_x][self.player1_y] != 0:
                      return 0
                  if self.team1[self.player1_x][self.player1_y + 1] != 0:
                      return 0
          elif self.player1_picking == 3: #ship 3
              if self.player1_dimension == vertical:
                  if self.team1[self.player1_x][self.player1_y] != 0:
                      return 0
                  if self.team1[self.player1_x + 1][self.player1_y] != 0:
                      return 0
                  if self.team1[self.player1_x + 2][self.player1_y] != 0:
                      return 0
              elif self.player1_dimension == horizontal:
                  if self.team1[self.player1_x][self.player1_y] != 0:
                      return 0
                  if self.team1[self.player1_x][self.player1_y + 1] != 0:
                      return 0
                  if self.team1[self.player1_x][self.player1_y + 2] != 0:
                      return 0
      
      
      elif id == '2':
          if self.player2_picking == 1:
              if self.team2[self.player2_x][self.player2_y] != 0:
                  return 0
          elif self.player2_picking == 2:
              if self.player2_dimension == vertical:
                  if self.team2[self.player2_x][self.player2_y] != 0:
                      return 0
                  if self.team2[self.player2_x + 1][self.player2_y] != 0:
                      return 0
              elif self.player2_dimension == horizontal:
                  if self.team2[self.player2_x][self.player2_y] != 0:
                      return 0
                  if self.team2[self.player2_x][self.player2_y + 1] != 0:
                      return 0
                      
          elif self.player2_picking == 3:
              if self.player2_dimension == vertical:
                  if self.team2[self.player2_x][self.player2_y] != 0:
                      return 0
                  if self.team2[self.player2_x + 1][self.player2_y] != 0:
                      return 0
                  if self.team2[self.player2_x + 2][self.player2_y] != 0:
                      return 0
                  
              elif self.player2_dimension == horizontal:
                  if self.team2[self.player2_x][self.player2_y] != 0:
                      return 0
                  if self.team2[self.player2_x][self.player2_y + 1] != 0:
                      return 0
                  if self.team2[self.player2_x][self.player2_y + 2] != 0:
                      return 0

      return 1

    #ham ban thuyen thuc hien:
    # + nhan du lieu va xu li
    # + thay doi gia tri trong mang 2 chieu
    # + thay doi gia tri trong database
    def fire_ship(self, id):
      if id == '1': # xet doi thu la id 2
        if (self.team2[self.player1_x][self.player1_y] == 3):
          self.database.update_status(str(self.player1_x * 10 + self.player1_y + 100), 'FIRE')
          self.player2_hit += 1
        else:
          self.database.update_status(str(self.player1_x * 10 + self.player1_y + 100), 'X')
      elif id == '2': # xet doi thu la id 1
        if (self.team1[self.player2_x][self.player2_y] == 3):
          self.database.update_status(str(self.player2_x * 10 + self.player2_y), 'FIRE')
          self.player1_hit += 1
        else:
          self.database.update_status(str(self.player2_x * 10 + self.player2_y), 'X')
      
      if self.player1_hit == 6:
        self.database.update_status_player(player='player1', value='lose', room=3)
        self.database.update_status_player(player='player2', value='win', room=3)
        print('team 2 WIN!')
      if self.player2_hit == 6:
        self.database.update_status_player(player='player1', value='win', room=3)
        self.database.update_status_player(player='player2', value='lose', room=3)
        print('team 1 WIN!')
