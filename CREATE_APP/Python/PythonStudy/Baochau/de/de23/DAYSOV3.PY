# sap xep day theo thu tu tang dan
def sap_sep(arr):
    arr.sort()
# đếm số lần xuất hiện của x trong dãy
def dem_so(arr, x):
    dem = 0
    for num in arr:
        if num == x:
            dem += 1
    return dem
# đếm số phần tử nhỏ hơn hoặc bằng x
def dem_nhohon(arr, x):
    dem = 0
    for num in arr:
        if num <= x:
            dem += 1
    return dem
# dếm số phần tử lớn hơn x:
def dem_lonhon(arr, x):
    dem = 0
    for num in arr:
        if num >x:
            dem += 1
    return dem

# nhập vào sanh sách và gọi các hàm
n = int(input('nhap so phan tu cua day: '))
arr = []
for i in range(n):
    num = int(input('nhap phan tu thu {}: '.format(i+1)))
    arr.append(num)

# sắp xếp theo thứ tự tăng dần
sap_sep(arr)
# nhập số x
x = int(input('nhap x: '))
# đém số lần xuất hiện của x trong dãy
dem_xh = dem_so(arr, x)
# đếm số phần tử nhỏ hơn hoặc bằng x
dem_nho = dem_nhohon(arr, x)
# đếm số phần tử lớn hơn x
dem_lon = dem_lonhon(arr, x)
# in kết quả ra màn hình
print('day so sau khi sap xep: ', arr)
print('so lan xuat hien cua x: ', dem_xh)
print('so phan tu nho hon hoac bang x: ', dem_nho)
print('so phan tu lon hon x: ', dem_lon)