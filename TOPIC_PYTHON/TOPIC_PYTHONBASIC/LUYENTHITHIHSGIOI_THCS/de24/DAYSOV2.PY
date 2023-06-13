def sort_odd_even(numbers):
    odd_numbers = []
    even_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    odd_numbers.sort()  # Sắp xếp phần tử lẻ tăng dần
    even_numbers.sort(reverse=True)  # Sắp xếp phần tử chẵn giảm dần

    sorted_numbers = odd_numbers + even_numbers  # Kết hợp danh sách số lẻ và số chẵn

    return sorted_numbers


# Nhập dãy số từ người dùng
n = int(input("Nhập số phần tử của dãy số: "))
numbers = []
for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i + 1}: "))
    numbers.append(num)

# Sắp xếp dãy số
sorted_numbers = sort_odd_even(numbers)

# In kết quả ra màn hình
print("Danh sách sau khi sắp xếp:")
for num in sorted_numbers:
    print(num, end=" ")
