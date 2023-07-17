def ucln(a,b):
    r = a%b
    while r!=0:
        a = b
        b = r
        r = a%b
    return b

f_in = open('UCLN.INP','r'); f_out = open('UCLN.OUT','w')
line = f_in.readline().split()
int_a = [int(x) for x in line]
uocchunglonnhat = ucln(int_a[0], int_a[1])
f_out.write(str(round(uocchunglonnhat,0)))
f_in.close(), f_out.close()