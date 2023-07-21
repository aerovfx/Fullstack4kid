#Hàm
def bieuthuc(n, x, y):
    kq = 0
    for i in range(1, n):
        kq += x ** i + y / i
    return kq
#Nhập n,x,y từ file:
f_in = open("BAI6.INP","r")
f_out = open("BAI6.OUT","w")
n = f_in.readline().split()
x, y = f_in.readline().split()
#In kết quả
f_out.write(bieuthuc(n, x, y))
f_in.close()
f_out.close()