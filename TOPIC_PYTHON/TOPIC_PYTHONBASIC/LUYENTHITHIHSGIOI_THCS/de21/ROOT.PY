import math #Dòng này import module math, cho phép sử dụng hàm math.sqrt() để tính căn bậc hai.

# Đọc dữ liệu từ file ROOT.INP
with open("ROOT.INP", "r") as file:
    lines = file.readlines()
    a = int(lines[0])
    b = int(lines[1])
    c = int(lines[2])
#Dòng này mở file ROOT.INP và đọc dữ liệu từ file. 
#Dữ liệu đọc được được lưu vào biến lines dưới dạng danh sách các dòng.
#Sau đó, lần lượt gán giá trị của a, b, c bằng các phần tử trong lines (chuyển đổi thành số nguyên).

# Tính giá trị của biểu thức S
S = (a**2 + b**2 + c**2) / (a*b*c) + math.sqrt(a*b*c)

# Ghi kết quả vào file ROOT.OUT
with open("ROOT.OUT", "w") as file:
    file.write("{:.2f}".format(S))
# Dòng này mở file ROOT.OUT và ghi kết quả tính toán S vào file. 
# Kết quả được định dạng làm tròn đến 2 chữ số sau dấu phẩy 
# và được ghi dưới dạng chuỗi bằng cách sử dụng phương thức format() và write().