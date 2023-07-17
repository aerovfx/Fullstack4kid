# hàm tìm số lớn nhất trong cặp
def sosanh(a,b):
    sosanh = int(max(a,b))
    return sosanh

# đọc file
with open('SOSANH.INP', 'r') as file:
    pair = file.read().strip().split(' ')
    
a,b = pair
# in dữ liệu
with open('SOSANH.OUT', 'w') as file:
    result = sosanh(a,b)
    file.write(f'{result}\n')