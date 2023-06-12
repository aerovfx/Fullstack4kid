def sort_array(arr):
    # Sắp xếp dãy theo thứ tự tăng dần
    arr.sort()

def count_occurrences(arr, x):
    # Đếm số lần xuất hiện của x trong dãy
    count = 0
    for num in arr:
        if num == x:
            count += 1
    return count

def count_elements_smaller(arr, x):
    # Đếm số phần tử nhỏ hơn hoặc bằng x
    count = 0
    for num in arr:
        if num <= x:
            count += 1
    return count

def count_elements_greater(arr, x):
    # Đếm số phần tử lớn hơn x
    count = 0
    for num in arr:
        if num > x:
            count += 1
    return count

# Nhập dãy số từ người dùng
n = int(input("Nhập số phần tử của dãy: "))
arr = []
for i in range(n):
    num = int(input("Nhập phần tử thứ {}: ".format(i + 1)))
    arr.append(num)

# Sắp xếp dãy theo thứ tự tăng dần
sort_array(arr)

# Nhập số x
x = int(input("Nhập số x: "))

# Đếm số lần xuất hiện của x trong dãy
occurrences = count_occurrences(arr, x)

# Đếm số phần tử nhỏ hơn hoặc bằng x
count_smaller = count_elements_smaller(arr, x)

# Đếm số phần tử lớn hơn x
count_greater = count_elements_greater(arr, x)

# In kết quả ra màn hình
print("Dãy sau khi sắp xếp: ", arr)
print("Số lần xuất hiện của x: ", occurrences)
print("Số phần tử nhỏ hơn hoặc bằng x: ", count_smaller)
print("Số phần tử lớn hơn x: ", count_greater)
