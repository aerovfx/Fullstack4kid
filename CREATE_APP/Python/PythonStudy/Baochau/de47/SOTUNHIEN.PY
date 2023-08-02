def is_prime(N):
    if N < 2:
        return False
    for i in range(2, int(N**0.5) +1):
        if N % i == 0:
            return False
        return True
            
def tong_songto(N):
    tong_ngto = []
    for i in range(2, N // 2 + 1):
        if is_prime(i) and is_prime(N - i):
            phuong_an = (i, N - i)
            if phuong_an not in tong_ngto:
                tong_ngto.append(phuong_an)
    return tong_ngto  

N = int(input('nhập số N(N<5000):'))
if N >= 5000:
    print('thông số N ko hợp lệ')
    
print('',tong_songto(N))
