a = input('nhập vào số nguyên a:')
b = input('nhập vào số nguyên b:')
a = int(a)
b = int(b)

def ucln(a,b):
    r = a%b
    while r != 0:
        a = b
        b = r
        r = a%b
    return b
result = ucln(a,b)
print('ước chúng lớn nhất là: ',result)