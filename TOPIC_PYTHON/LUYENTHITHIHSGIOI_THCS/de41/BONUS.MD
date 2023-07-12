Đề sơ khảo quốc gia 2020
An là người thắng cuộc trong cuộc thi "TÌm hiểu Đoàn thanh niên Cộng sản Hồ Chí Mình" và được nhận phần thưởng của Ban tổ chức. Ban tổ chức chuẩn bị một bảng kích thước mxn. Các dòng của bảng được đánh số từ 1 đến m, từ trên xuống dưới, dòng i ( 1<= i <= m) có trọng số là a. Các cột của hàng được đánh số từ 1 đến n, từ trái qua phải, cột j (1 <= j <= n) có trọng số là b. Ô nằm trên giao của dòng i và cột j được gọi là ô (i,j) và trên ô đó ghi một số nguyên có giá trị a + b.
Để nhận phần thưởng, An được phép chọn một bảng con kích thức wxh chiếm trong wxh ô của bảng và phần thưởng mà An nhận được sẽ có giá trị bằng tổng giá trị các ô nằm trong bảng con đó.

Yêu cầu: Hãy xác định tổng giá trị lớn nhất mà An có thể nhân được.
Dữ liệu: vào từ file văn bản BONUS.INP
+Dòng thứ nhất chứa bốn số nguyên dược m,n,ư,h (w <= n, h <= n);
+Dòng thứ hai chứa m số nguyên a_1, a_2, ....,a_n (|a| <= 10^6, i = 1,2,3,...,m);
+Dòng thứ ba chứa n số nguyên b_1, b_2,.....,b_n (|b| <= 10^6, i = 1,2,3,...,n);

Kết qủa: Ghi ra file văn bản BONUS.OUT một số nguyên duy nhất là tổng giá trị lớn nhất mà An có thể nhận được.
Ràng buộc:
+Có 20% số test ứng với m, n <= 10 và w = h = 1;
+Có 30% số test khác ứng với m, n <= 10;
+Có 20% số test khác ứng với m, n <= 10^3;
+Có 30% số test còn lại có m, n <=10^5;

Ví dụ:
BONUS.INP
3 4 2 2
1 -1 2
1 1 1 1

BONUS.OUT
6

Giải thích
Bảng ma trận có kích thước 3x4, trọng số của các hàng và các cột đươcj ghi trong ngoặc ở hàng và cột tương ứng. Cách chọn bảng con kích thước 2x3 là hình được tô màu và có tổng giá trị là 6.
2 2 2 2
0 0 0 0
3 3 3 3
Bảng con mà An chọn
0 0
3 3

Xem hình 
<img width="375" alt="Screenshot 2023-07-10 at 07 24 26" src="https://github.com/aerovfx/Fullstack4kid/assets/109997053/82acfaa7-336d-43db-a3ee-e3e8f9decd18">

