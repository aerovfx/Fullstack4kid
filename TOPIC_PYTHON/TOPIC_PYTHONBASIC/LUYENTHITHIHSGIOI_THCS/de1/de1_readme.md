CHU THICH BAI 1
Đây là đoạn code Python để tính diện tích hình vuông tạo bởi một tam giác vuông, nếu tam giác không phải là tam giác vuông thì trả về giá trị -1.

Dòng 1-6: Định nghĩa hàm S_hv(a,b,c) với các tham số a, b, c là ba cạnh của tam giác. Hàm này sẽ kiểm tra xem tam giác có phải tam giác vuông hay không và trả về diện tích của hình vuông tạo bởi tam giác vuông đó, nếu không trả về -1.
Dòng 8-9: Mở file "TAMGIAC.INP" để đọc vào các giá trị cạnh của tam giác.
Dòng 10: Đọc dòng đầu tiên của file và chia thành một mảng các chuỗi.
Dòng 12: Tạo một mảng mới int_a từ mảng chuỗi vừa đọc và chuyển các giá trị thành kiểu số nguyên.
Dòng 13: Gọi hàm S_hv với ba tham số là ba cạnh của tam giác được lưu trong int_a.
Dòng 14: Ghi giá trị của diện tích hình vuông vào file "TAMGIAC.OUT" với độ chính xác 1 chữ số thập phân.
Dòng 15-16: Đóng cả hai file đang mở.




Chu thich bai 3

Dòng 1: Mở file "CARO3D.INP" trong chế độ đọc dữ liệu.
Dòng 2: Mở file "CARO3D.OUT" trong chế độ ghi dữ liệu.
Dòng 4-9: Đọc ma trận 2 chiều có kích thước 6x7 từ file input "CARO3D.INP" và lưu vào biến a. Trong đó, mỗi phần tử của ma trận là một số nguyên được đọc từ file input.
Dòng 11-21: Tính toán số lượng cờ liên tiếp theo chiều ngang trong ma trận a và số lượng thắng theo từng người chơi (người chơi 1 và người chơi 2). Nếu có 4 cờ liên tiếp cùng một giá trị trong một hàng, thì tương ứng với người chơi nào thắng, số lượng thắng của người chơi đó sẽ được tăng lên 1.
Dòng 23-33: Tính toán số lượng cờ liên tiếp theo chiều dọc trong ma trận a và số lượng thắng theo từng người chơi (người chơi 1 và người chơi 2). Nếu có 4 cờ liên tiếp cùng một giá trị trong một cột, thì tương ứng với người chơi nào thắng, số lượng thắng của người chơi đó sẽ được tăng lên 1.
Dòng 35-39: Kiểm tra và ghi kết quả vào file output "CARO3D.OUT" theo yêu cầu đề bài. Nếu cả hai người chơi đều thắng hoặc không ai thắng, ghi "-1". Nếu người chơi 1 thắng, ghi "1". Nếu người chơi 2 thắng, ghi "0".
Dòng 41-42: Đóng file input và file output.