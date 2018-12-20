<?php
if((isset($_POST["room"])) && (isset($_POST["min"])) && (isset($_POST["max"]))) {
	$room = $_POST["room"];
	$min = $_POST["min"];
	$max = $_POST["max"];

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

	$sql = "SELECT id_square, SHIPVALUE 
	FROM GAMESTATUS  
	WHERE ROOM='$room' && id_square>='$min' && id_square<='$max'
	ORDER BY id_square ASC";
	$result = $connect->query($sql);

	if(!$result) {
	    die("Error query Users database".$connect->connect_error);
	    exit();
	}

	//Tham chieu den tung phan tu trong table
	$data=array();
	$row;
	while ($row = $result -> fetch_array(MYSQLI_ASSOC)) {
		$data[]=$row;
	}
	$connect->close();
		
		
	echo json_encode($data);
}
?>
