n = int(input('Nhap n: '))

while n <= 0:
    n = int(input('Nhap n: '))

gt = 1

while n > 0:
    gt = gt * n
    n = n - 1

print('Giai thua cua n la:', gt)