# hàm tìm số lớn nhất trong cặp
def ptb1(a,b):
    if a == 0:
        return ('vo nghiem')
    else:
        return -b/a

# đọc file
with open('PTB1.INP', 'r') as file:
    numbers = file.readlines()

results = []
for num in numbers:
    pt = num.strip().split(' ')
    nghiem_list = list(map(int, pt)) # chuyển đổi thành danh sách số nguyên
    result = ptb1(*nghiem_list) # used hàm maxnum() để tìm giá trij lớn nhất
    results.append(result)

# in dữ liệu
with open('PTB1.OUT', 'w') as file:
    for result in results:
        file.write(f'{result}\n')