from math import sqrt
a = input('nhap so thu nhat:')
s = int(a)
a = input('nhap so thu hai:')
s = s*int(a)
a = input('nhap so thu ba:')
s = s*int(a)
a = input('nhap so thu tu:')
s = s*int(a)
print('trung binh nhan cua bon so la:', sqrt (sqrt(s)))