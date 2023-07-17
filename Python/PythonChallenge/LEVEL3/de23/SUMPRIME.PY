def nguyen_to(num):
    if num <2 :
        return False
    for i in range(2, int(num**0.5) + 1):
        if num% i == 0:
            return False
    return True

def tong_so_ngto(A,B):
    so_ngto = []
    tong_ngto = 0
    for num in range(A, B+1):
        if nguyen_to(num):
            so_ngto.append(num)
            tong_ngto += num
    return so_ngto, tong_ngto

# đọc dữ liệu
with open('SUMPRIME.INP', 'r') as file:
    A,B = map(int, file.readlines().split())
    
so_ngto, tong_ngto = tong_so_ngto(A,B)

# in dữ liệu
with open('SUMPRIME.OUT', 'w') as file:
    file.write('day so nguyen to: \n')
    file.write(''.join(str(num) for num in so_ngto))
    file.write('\n tổng dãy số nguyên tố là: ')
    file.write(str(tong_ngto))