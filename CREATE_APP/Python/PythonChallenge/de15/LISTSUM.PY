# đọc dữ liệu vào
with open('LISTSUM.INP', 'r') as file:
    numbers = file.readlines()


result = []
for num in numbers:
    tong_list = num.strip().split(' ')
    tong = sum(map(int, tong_list))
    result.append(tong)
 

with open('LISTSUM.OUT', 'w') as file:
    file.write(str(result))
