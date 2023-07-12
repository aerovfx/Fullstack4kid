Dựa vào dữ liệu trên, ta có các bước thực hiện như sau:
1. Đọc dữ liệu từ file "BONUS.INP".
2. Khởi tạo ma trận dp với kích thước (m+1) x (n+1) và giá trị ban đầu là 0.
3. Duyệt qua từng ô của ma trận dp:
   4. Duyệt qua từng hàng và cột của ma trận dp (từ 1 đến m và từ 1 đến n):
      5. Khởi tạo biến total = 0.
      6. Duyệt qua các hàng và cột của bảng con kích thước wxh, có gốc tại ô (i, j):
         7. Kiểm tra xem hàng và cột nằm trong phạm vi của ma trận ban đầu (x <= m và y <= n).
         8. Tính tổng giá trị của các ô trong bảng con và cập nhật vào biến total.
      9. Cập nhật giá trị tối đa cho ô (i, j) trong ma trận dp.
10. Lấy giá trị tại ô cuối cùng dp[m][n] là kết quả tổng giá trị lớn nhất mà An có thể nhận được.
11. Ghi kết quả vào file "BONUS.OUT".


Khởi tạo ma trận dp với kích thước (m+1)x(n+1) và giá trị ban đầu là 0:

dp = [
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0]
]
Duyệt qua từng ô của ma trận dp:
Với i = 1 và j = 1:
Tính tổng giá trị của bảng con kích thước 2x2, có gốc tại ô (1, 1):
total = a[0] + b[0] + a[1] + b[1] = 1 + 1 + (-1) + 1 = 2
Cập nhật giá trị tối đa cho ô (1, 1):
dp[1][1] = max(dp[1][0], dp[0][1], dp[0][0] + total) = max(0, 0, 0 + 2) = 2
Tiếp tục duyệt qua các ô còn lại trong ma trận dp và thực hiện các bước tương tự.
Kết quả cuối cùng sẽ là giá trị tại ô cuối cùng dp[m][n]:

Với i = 3 và j = 4:

result = dp[3][4] = 6
Vậy, với các giá trị cụ thể của vòng lặp i và j trong ví dụ này, kết quả là 6.
