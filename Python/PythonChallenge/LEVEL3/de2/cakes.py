a = []
def chia_banh(n):
    for i in range(1, int(n)+1):
        if n % i == 0:
            a.append(i)
    return a

# đọc dữ liệu tùe file
with open('CAKES.INP', 'r') as file:
    n = int(file.readline().strip())
    
result = chia_banh(n)

# ghi dữ liệu vào file
with open('CAKES.OUT', 'w') as file:
    for num in result:
        file.write(f'{num}\n')
        