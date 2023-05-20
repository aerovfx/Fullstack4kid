Xem tại link:
https://docs.google.com/document/d/18AYWxDsFyhr9XoE68ujlnd-iBkqEJUWHW8ogQeU2RkY/edit?usp=sharing

PHÒNG GIÁO DỤC VÀ ĐÀO TẠO, HUYỆN BẢO LÂM
Ky thi cho hoc sinh gioi cap huyen mon tin hoc 9 
2020-202
1hhoi gian 150 phut

CÂÚ TRÚC ĐỀ

Câu 1: (6 điểm)
Diện tích tam giác vuông
Cho 3 số tự nhiên a, b, c (0 <a, b, c<10^6). 
Hãy viết chương trình tính diện tích tam giác nếu ba số đã cho là ba cạnh của một tam giác vuông.
Dữ liệu vào từ file: TAMGIAC.INP
-Dòng đầu tiện ghi ba số tự nhiên a,b, c. Các số đó phải cách nhau 1 khoảng trắng.
Kết qủa ra file: TAMGIAC.OUT
-Dòng đầu tiên ghi diện tích tính được (làm tròn một chữ số thập phân), nếu ba số đã cho không phải là ba cạnh của tam giác vuông thì ghi số -1
Ví du:
-----------------------------------------------
| TAMGIAC.INP       | TAMGIAC.OUT             |
| 3 4 5             | 6.0                     |
| 3 4 9             | -1                      |
-----------------------------------------------

Câu 2: 7 điểm.
Với lịch dương thì các tháng cos 31 ngày là 1, 3, 5, 7, 8, 10, 12 và các tháng có 30 ngày là 4, 6, 9 ,11. Riêng tháng 2 có thể có 28 hoặc 29 ngày tuỳ theo năm.
Từ năm 2012 đến năm 2099, các năm chia hết cho 4 đều là năm nhuận và tháng 2 của năm nhuận có thể có thêm ngày thứ 29.
Cho bộ ba số [d1, m1, y1] và [d2,m2,y2], mỗi bộ 3 số lần lượt là ngày tháng năm (2012 <= y1, y2 <= 2099).
Hãy viết chương trình tính số ngày trong khoảng thời gian được cho.
Dữ liệu vào từ file là: SONGAYINP
-Hai dòng đầu, mỗi dòng ghi lần lượt ba số là ngày, tháng và năm, các số cách nhau khoảng trắng.
Kết quả ra file: SONGAY.OUT
-Dòng đầu tiên ghi số ngày tính được.
Ví dụ:

-----------------------------------------------
| SONGAY.INP       | SONGAY.OUT.              |
| 25 1 2012        | 61                       |
| 26 3 2012        |                          |
-----------------------------------------------
| 20 1 2018        | 1035                     |
| 20 11 2020       |                          |
-----------------------------------------------

CÂU 3: (7 điểm) Connect four

Connect four là trò cờ Caro 3D, nó rèn luyện tư duy toán học, thường được làm từ vật liệu gỗ thân thiện với môi trường, không độc hại và không gây kích ứng, an toàn và lành mạnh cho trẻ em.
Luật chơi cho các bé dưới 5 tuổi rất đơn gian như sau: Có hai bé cùng chơi, mỗi bé có 21 quân cơ màu đỏ hoặc màu vàng, khi chơi bé luân phiên thả các quân cờ vào trong 7. hàng dọc, mỗi hàng chứa được 6 quân cờ, cho đến khi thả hết các quân cờ.
Bé nào đạt được 4 quân cờ trở lên nối liền nhau theo chiều ngang hoặc chiều dọc sẽ chiến thắng. 
Nếu 2 bé cùng dược hoặc cùng không được 4 quân cờ trở lên nối liên nhau sẽ hoà.
Ta kí hiêu số 1 là đại diện quân cờ đỏ, số 0 là đại diện quân cờ vàng. Hãy viết chương trình xác định kết quả trò chơi của hai bé?
Dữ liệu vào từ file: CARO3D.IND
-Gồm 6 dòng, mỗi dòng lần lượt ghi 7 số 0 hoặc 1 các số cách nhau một khoảng trắng dùng để mô tả vị trí chứ các quân cờ trên bàn cờ Connect four.
Kết quả ra file: CARO.OUT
-Đòng đầu tiên ghi kết quả trò chơi như sau:
Nếu quân đỏ thắng thì ghi 1, nếu quân vàng thắng thì ghi 0, hoà thì ghi -1.
Ví dụ:

-----------------------------------------------
| CARO3D.INP       | CARO3D.OUT.              |
| 1 0 1 0 1 0 0    | 0                        |
| 1 1 1 0 1 1 0    |                          |
| 1 0 1 0 0 0 0    |                          |
| 1 1 0 1 1 0 1    |                          |
| 1 1 0 1 1 0 0    |                          |
| 1 0 1 0 1 0 0    |                          |
-----------------------------------------------
| 1 0 1 0 1 0 1    | -1                       |
| 1 1 1 0 1 1 0    |                          |
| 1 0 1 0 0 0 0    |                          |
| 1 0 1 1 1 0 1    |                          |
| 1 0 0 1 1 0 0    |                          |
| 1 0 1 0 1 0 0    |                          |
-----------------------------------------------


Họ và tên thí sinh:............Số báo danh:...........
