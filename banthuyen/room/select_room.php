<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] == 'GET') {
	if(!empty($_GET["room"])) {
		if ($_GET["room"] == 'null'){
			$_SESSION["Room"] = null;
		}
		else {
			$_SESSION["Room"] = $_GET["room"];
		}
	}
}

if(!isset($_SESSION["User"])) { //chua dang nhap
	header('Location: ../log/login.php');
}

if(!isset($_SESSION["Room"])) { //da dang nhap chua chon phong?>
<!DOCTYPE html>
<html>
<head>
	<title>Select Room</title>
</head>
<body>
<div>
	<p style="color:Tomato; font-size:300%;">Room 1</p>
	<img src="room.jpg" heigh=300 width=500></img>

	<p>--------------------------------------------------------------------------------------------------------------------------------------------------</p>

	<p style="color:Tomato; font-size:300%;">Room 2</p>
	<img src="room.jpg" heigh=300 width=500></img>

	<p>--------------------------------------------------------------------------------------------------------------------------------------------------</p>

	<a href="select_room.php?room=3"><p style="color:Tomato; font-size:300%;">Room 3</p></a>
	<a href="select_room.php?room=3"><img src="room.jpg" heigh=300 width=500"></img></a>

	<p>--------------------------------------------------------------------------------------------------------------------------------------------------</p>

	<p style="color:Tomato; font-size:300%;">Room 4</p>
	<img src="room.jpg" heigh=300 width=500></img>

	<p>--------------------------------------------------------------------------------------------------------------------------------------------------</p>

	<p style="color:Tomato; font-size:300%;">Room 5</p>
	<img src="room.jpg" heigh=300 width=500></img>
</div>
</body>
</html>
<?php 
}
if (isset($_SESSION["User"]) && isset($_SESSION["Room"]))
	header('Location: ../matrix.php');
?>