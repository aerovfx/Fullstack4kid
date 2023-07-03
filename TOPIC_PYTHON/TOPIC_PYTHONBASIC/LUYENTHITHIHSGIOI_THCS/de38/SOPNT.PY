# Hàm tìm số ước số của một số nguyên dương n
def pnt(n):
    d = 2
    for i in range(2, n):
        if n % i == 0:
            d += 1
    return d

# Hàm tìm số phản nguyên tố
def sopnt(n):
    max_val = pnt(1)
    num = 1
    for i in range (2, n + 1):
        if max_val < pnt(i):
            max_val = pnt(i)
            num = i
    return num

# Đọc dữ liệu từ file
with open("SOPNT.INP","r") as f:
    lines = f.readlines()
    k_values = [int(line.strip()) for line in lines[1:]]


# Gọi hàm số phản nguyên tố và gán cho 1 danh sách kết quả
results = [sopnt(k) for k in k_values]


# Ghi dữ liệu ra file
with open("SOPNT.OUT","w") as f:
    for num in results:
        f.write(str(num) + "\n")

