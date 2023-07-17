# hàm tìm ucln cua a,b
def ucln(a,b):
    if b == 0:
        return a
    return ucln(b, a%b)
"""import math"""
# dọc dử liệu từ file
with open('CHINHPHUONG.INP', 'r') as file:
    n = int(file.readline())
    a = list(map(int, file.readline().split()))

P = 1
for i in range(n):
    P = P*a[i] //ucln(P, a[i])
# tính phần dư của phép chia P cho 10^9 + 7
result = P ** 2 % ( 10**9 + 7)
# in dữ liệu
with open('CHINHPHUONG.OUT', 'w') as file:
    file.write(str(result))