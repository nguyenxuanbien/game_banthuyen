----------------------------------vao phong choi game----------------------------------
- Dau tien vao matrix.php de choi
- Neu chua dang nhap se chuyen den trang dang nhap
- Nhap user & passw 1 trong 2 tai khoan sau:
     - user: player1
     - pass: player1

     - user: player2
     - pass: player2
- Chon room (chi co the chon duoc room 3)
----------------------------------flow front-end--------------------------------------------------
* chi ap dung voi room 3
* matrix.php sẽ gửi post request liên tục mỗi giay tới get_data_database.php
	+ ma trận 1 (container1)
		request bao gồm (room=3 & min=0 & max=99), ô vuông từ 0-99 (tính từ phải qua trái, từ trên xuống dưới)
	+ ma trận 2 (container2)
		request bao gồm (room=3 & min=100 & max=199), ô vuông từ 100-199

* sau khi nhan response sẽ truyền vào hàm grid (trong matrix.js) thông qua biến data.
* hàm grid xử lí xong sẽ show hình ảnh ra page
----------------------------------cau truc database-----------------------------------------------

		$username="battleship";
	    $password="qwerty12345678";
	    $server = "localhost";
	    $dbname = "BATTLESHIP";

* bang gamestatus:
- id int(6) auto incre
- id_square int(6) (chạy từ 0 đến 199)
- SHIPVALUE varchar(20) gồm:
	+"0" ô trống
	+"SHIP" có thuyền
	+"SHIP+SELECT" có thuyền được chọn
	+"SELECT" ô được chọn
	+"FIRE" bị bắn trúng
	+"X" bị bắn hụt
- ROOM varchar(2) chỉ toàn 3

* bang user:
- id int(6) auto incre
- USERNAME varchar(30) có:
	+"player1"
	+"player2"
- PASSWORD varchar(30) có:
	+"player1"
	+"player2"