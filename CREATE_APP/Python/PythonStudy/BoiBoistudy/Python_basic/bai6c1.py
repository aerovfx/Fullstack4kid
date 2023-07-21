#Hàm
def bieuthuc(n, x, y):
    result = 0
    for i in range(2, n + 1):
        result += x ** i + y / i
    return result
#Nhập n,x,y từ bàn phím
n = int(input('Nhập vào n: '))
x = int(input('Nhập vào x: '))
y = int(input('Nhập vào y: '))
#In ra kết quả
print(bieuthuc(n, x, y))
