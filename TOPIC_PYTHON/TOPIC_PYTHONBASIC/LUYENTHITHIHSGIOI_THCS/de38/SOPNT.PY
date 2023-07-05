# hàm tìm ước số của một số nguyên dương n
def uocso(n):
    d = 2
    for i in range(2, n):
        if n % i == 0:
            d += 1
    return d
    
""" Hàm uocso(n) được sử dụng để đếm số ước số của một số nguyên dương n. 
Biến d được khởi tạo ban đầu là 2 vì mỗi số nguyên dương đều có ít nhất hai ước số là 1 và chính nó. 
Hàm này duyệt qua các số từ 2 đến n-1 và kiểm tra nếu n chia hết cho số đó thì tăng biến d lên 1. 
Cuối cùng, hàm trả về giá trị của biến d, tức là số ước số của n.
"""
# hàm tìm số phản ngto
def phanngto(n):
    max_value = uocso(1)
    num = 1
    for i in range(2, n+1):
        if max_value < uocso(i):
            max_value = uocso(i)
            num = i
    return num
# đọc dữ liệu
with open('SOPNT.INP', 'r') as file:
    lines = file.readlines()
    k_value = [int(line.strip()) for line in lines[1:]]

# gọi hàm
results = [phanngto(k) for k in k_value]
    
# in dữ liệu
with open('SOPNT.OUT', 'w') as file:
    for num in results:
        file.write(str(num) + '\n')