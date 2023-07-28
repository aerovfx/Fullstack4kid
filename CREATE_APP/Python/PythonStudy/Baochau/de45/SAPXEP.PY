n = int(input('nhập vào số phần tử: '))
danh_sach = list(map(int, input('nhập các phàn tử, các số cách nhau dấu cách: '))).split()
k = int(input('nhập vào số nguyên k:'))

danh_sach.sort(reverse=True)

for i in range(len(danh_sach)):
    if k >= danh_sach[i]:
        danh_sach.append(i, k)


print('sắp xếp giảm dần: '.join(map(str, danh_sach)))
print('sắp xếp khi có k:',)