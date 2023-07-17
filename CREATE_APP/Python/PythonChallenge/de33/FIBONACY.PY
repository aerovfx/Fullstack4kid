def fibonacy(n):
    danh_sach = [1,1] # tao danh sach fibo voi 2 
    for i in range(2, n):
        fibo = danh_sach[i-1] + danh_sach[i-2]
        danh_sach.append(fibo)
    return danh_sach

n = int(input('nhap so n: '))
result = fibonacy(n)
print(n,' so fibonacy dau tien: ',result )
# in ra số fibonacy nhỏ hơn hoặc bằng n
n = int(input('nhap so n: '))
fibo_num = []
a,b = 1,1 
while a<=n:
    fibo_num.append(a)
    a,b = b, a+b
print('cac số fibo nhỏ hơn hoặc bằng',n,':',fibo_num)
