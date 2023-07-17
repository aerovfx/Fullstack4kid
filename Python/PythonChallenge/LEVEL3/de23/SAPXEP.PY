def sap_xep(numbers):
    odd = []
    even = []
    
    for num in numbers:
        if num%2 == 0:
            even.append(num)
        else:
            odd.append(num)
            
    odd.sort()
    even.sort(reverse=True)
    sap_xep_so = odd + even
    return sap_xep_so
n = int(input('nhap so phan tu trong day so: '))
numbers = []
for i in range(n):
    num = int(input(f'phan tu thu(i+1): '))
    numbers.append(num)
    
sap_xep_so = sap_xep(numbers)
print('danh sach cac so khi da sap xep la: ')
for num in sap_xep_so:
    print(num, end=' ')