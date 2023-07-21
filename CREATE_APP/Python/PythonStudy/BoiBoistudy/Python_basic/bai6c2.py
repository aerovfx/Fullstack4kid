#Hàm
def bieuthuc(n, x, y):
    result = 0
    for i in range(2, n + 1):
        result += x ** i + y / i
    return result
#Nhập n,x,y từ thân chương trình
n = 2
x = 1
y = 1
#In ra kết quả
print(bieuthuc(n, x, y))