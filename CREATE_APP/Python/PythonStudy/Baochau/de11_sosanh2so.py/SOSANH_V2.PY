# hàm tìm số lớn nhất trong cặp
def sosanh(a,b):
    sosanh = int(max(a,b))
    return sosanh

# đọc file
with open('SOSANH.INP', 'r') as file:
    numbers = file.readlines()

results = []
for num in numbers:
    maxnum = num.strip().split(' ')
    max_list = list(map(int, maxnum)) # chuyển đổi thành danh sách số nguyên
    result = sosanh(*max_list) # used hàm maxnum() để tìm giá trij lớn nhất
    results.append(result)

# in dữ liệu
with open('SOSANH.OUT', 'w') as file:
    for result in results:
        file.write(f'{result}\n')