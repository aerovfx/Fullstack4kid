
def giai_thua(n):
    if n == 0:
        return 1
    else:
        return n * giai_thua(n-1)
    
with open('GIAI_THUA.INP', 'r') as file:
    numbers = file.read()
    
result = []
for num in numbers:
    num = int(num)
    giai_thua_num = giai_thua(num)
    result = str(giai_thua_num)
    
with open('GIAI_THUA.OUT', 'w') as file:
    file.write(result)
    