<?php
if(isset($_POST["room"])) {
	$room = $_POST["room"];
	//database
	$username="battleship";
	$password="qwerty12345678";
	$server = "localhost";
	$dbname = "BATTLESHIP";

	$connect=new mysqli($server,$username,$password,$dbname);
	if ($connect->connect_error) {
	    die("Error connect database".$connect->connect_error);
	    exit();
	}
	/*----------------check user and password------------------*/
	$sql = "SELECT CURRENT_STEP FROM STEP WHERE ROOM='$room'";
	$result = $connect->query($sql);

	if(!$result) {
	    die("Error query Users database".$connect->connect_error);
	    exit();
	}
	
	$row = $result -> fetch_array(MYSQLI_ASSOC);
	echo $row['CURRENT_STEP'];
	$connect->close();
	
}
?>
