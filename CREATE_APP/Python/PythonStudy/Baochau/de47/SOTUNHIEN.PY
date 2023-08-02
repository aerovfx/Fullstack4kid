n = int(input('nhập số n (n<=5000):'))
if n >=5000:
    print('thông số n ko hợp lệ.')
    

def tong_n(n):
    for i in n:
        for j in n:
            tong = n[i] + n[j]
        if tong % 2 != 0:
            return n[i], n[j]
        
result = tong_n(n)
print('tổng 2 số nguyên tố n:', result)