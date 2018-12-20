<?php
session_start();
$_SESSION=array();
session_destroy();
?>
<!DOCTYPE html>
<html>
<head>
    <title>Log out</title>
</head>
<body>
<p>See You Again!</p>
<p><strong><a href="../matrix.php">Play</a></strong></p>
</body>
</html>