from array import *
n = input('nhap vao so nuyen duong n: ')
n = int(n)
# tao mang fibonacci co ten la fibo voi 2 chi so dau tien mac dinh 1,1
fibo = array('i', [1,1])
i = 2
a = 1
# chay vong lap voi dieu kien thoat la a>=n
while a<n:
    a = fibo[i-1] + fibo[i-2]
    print(a)
    fibo.append(a)
    i += 1


if fibo[i-1] == n: print('yes')
else: print('no')


