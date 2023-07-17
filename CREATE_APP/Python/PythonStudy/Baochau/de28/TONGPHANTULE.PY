# nhập vào số phần tử của dãy
n = int(input('nhập vào số phần tử của dãy: '))
# khởi tạo bién tổng lẻ
tong_le = 0

# tìm tổng các số lẻ
for i in range(n):
    num = int(input('phần tử thứ {}: '.format(i+1)))
    if num % 2 != 0:
        tong_le += num
# in ra kết quả
print('tổng các số lẻ: ',tong_le)