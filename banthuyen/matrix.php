<?php
session_start();
if(!isset($_SESSION["User"])) { //chua dang nhap
	header('Location: log/login.php');
}

if(!isset($_SESSION["Room"])) { //chua chon phong
	header('Location: room/select_room.php');
}

if (isset($_SESSION["User"]) && isset($_SESSION["Room"])) {
?>
<!DOCTYPE html>
<html>
<body>
<script src="matrix.js"></script> 
<div>
<span id="container1"></span>
<span>------</span>         
<span id="container2"></span>
</div>
<div>
<span id="coor" style="color:Tomato; font-size:300%;text-align:center;"></span>
</div>
<div id="result" style="color:Blue; font-size:300%;text-align:center;"></div>
<script type="text/javascript">
	var intervalId;
	var ajax_call;
	var player="<?php echo $_SESSION['User'];?>";
	var current_step=1;
	ajax_call = function() {
	/*---------------------Get database data-------------------*/
		var xhttp_status_player = new XMLHttpRequest();
		xhttp_status_player.onreadystatechange = function() {
			if (this.readyState == 4 && this.status == 200) {
				document.getElementById("result").innerHTML="";
				if(this.responseText=='win') {
					document.getElementById("result").innerHTML="Player1 Win, Player2 Lose";
				}
				else if(this.responseText=='lose') {
					document.getElementById("result").innerHTML="Player1 Lose, Player2 Win";
				}
				else {
					document.getElementById("result").innerHTML="Playing";
				}
			}
		};
		xhttp_status_player.open("POST", "get_status_player.php", true);
		xhttp_status_player.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		xhttp_status_player.send("room=3&player=player1");

		var xhttp_current_step = new XMLHttpRequest();
		xhttp_current_step.onreadystatechange = function() {
			if (this.readyState == 4 && this.status == 200) {
				current_step= this.responseText;
			}
		};
		xhttp_current_step.open("POST", "get_current_step.php", true);
		xhttp_current_step.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		xhttp_current_step.send("room=3");
		
		if(player=="player1") {
			var room_1_1="room=" + <?php echo json_encode($_SESSION['Room']); ?> +"&min=0&max=99";
			var xhttp_1_1 = new XMLHttpRequest();
			xhttp_1_1.onreadystatechange = function() {
				if (this.readyState == 4 && this.status == 200) {
				    var result_1_1 = JSON.parse(this.responseText);
				    document.getElementById("container1").innerHTML="";
				    var container1 = document.getElementById("container1");
				    container1.appendChild(grid(10, 70, 700, "blue", "coor", result_1_1,"false",current_step));
				}
			};
			xhttp_1_1.open("POST", "get_data_database.php", true);
			xhttp_1_1.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
			xhttp_1_1.send(room_1_1);
			

			
			var room_1_2="room=" + <?php echo json_encode($_SESSION['Room']); ?> +"&min=100&max=199";
			var xhttp_1_2 = new XMLHttpRequest();
			xhttp_1_2.onreadystatechange = function() {
				if (this.readyState == 4 && this.status == 200) {
				    var result_1_2 = JSON.parse(this.responseText);
				    document.getElementById("container2").innerHTML="";
				    var container2 = document.getElementById("container2");
				    container2.appendChild(grid(10, 70, 700, "blue", "coor", result_1_2,"true",current_step));
				}
			};
			xhttp_1_2.open("POST", "get_data_database.php", true);
			xhttp_1_2.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
			xhttp_1_2.send(room_1_2);
		}
		if(player=="player2") {
			var room_1_1="room=" + <?php echo json_encode($_SESSION['Room']); ?> +"&min=0&max=99";
			var xhttp_1_1 = new XMLHttpRequest();
			xhttp_1_1.onreadystatechange = function() {
				if (this.readyState == 4 && this.status == 200) {
				    var result_1_1 = JSON.parse(this.responseText);
				    document.getElementById("container1").innerHTML="";
				    var container1 = document.getElementById("container1");
				    container1.appendChild(grid(10, 70, 700, "blue", "coor", result_1_1,"true",current_step));
				}
			};
			xhttp_1_1.open("POST", "get_data_database.php", true);
			xhttp_1_1.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
			xhttp_1_1.send(room_1_1);
			

			
			var room_1_2="room=" + <?php echo json_encode($_SESSION['Room']); ?> +"&min=100&max=199";
			var xhttp_1_2 = new XMLHttpRequest();
			xhttp_1_2.onreadystatechange = function() {
				if (this.readyState == 4 && this.status == 200) {
				    var result_1_2 = JSON.parse(this.responseText);
				    document.getElementById("container2").innerHTML="";
				    var container2 = document.getElementById("container2");
				    container2.appendChild(grid(10, 70, 700, "blue", "coor", result_1_2,"false",current_step));
				}
			};
			xhttp_1_2.open("POST", "get_data_database.php", true);
			xhttp_1_2.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
			xhttp_1_2.send(room_1_2);
		}
	};

	start_interval(); //set timer

	function start_interval() {
		if (intervalId) {
		    clearInterval(intervalId);
		}
		intervalId = setInterval(ajax_call, 500);
	}
</script>
<a href="room/select_room.php?room=null"><p>Exit room</p></a>
<a href="log/logout.php"><p>Log out</p></a>
</body>
</html>

<?php } ?>
