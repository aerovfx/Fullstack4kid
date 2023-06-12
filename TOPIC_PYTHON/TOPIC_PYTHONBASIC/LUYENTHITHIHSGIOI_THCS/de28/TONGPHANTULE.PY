# Nhập số phần tử trong dãy
N = int(input("Nhập số phần tử trong dãy: "))

# Khởi tạo biến tổng
tong_le = 0

# Nhập dãy số và tính tổng các số lẻ
for i in range(N):
    num = int(input("Nhập số thứ {}: ".format(i + 1))) #được sử dụng để nhập giá trị của phần tử thứ i trong dãy từ người dùng.
    if num % 2 != 0:
        tong_le += num

# In ra kết quả tổng các số lẻ
print("Tổng các số lẻ trong dãy là:", tong_le)
