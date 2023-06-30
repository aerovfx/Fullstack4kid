def find_min_max(numbers):
    min_num = float('inf')  # Khởi tạo giá trị nhỏ nhất ban đầu
    second_min_num = float('inf')  # Khởi tạo giá trị nhỏ thứ hai ban đầu
    max_num = float('-inf')  # Khởi tạo giá trị lớn nhất ban đầu
    max_index = -1  # Khởi tạo vị trí lớn nhất ban đầu

    for i in range(len(numbers)):
        num = numbers[i]
        if num < min_num:
            second_min_num = min_num
            min_num = num
        elif num < second_min_num and num != min_num:
            second_min_num = num
        if num > max_num:
            max_num = num
            max_index = i

    return min_num, second_min_num, max_index


# Ví dụ sử dụng
numbers = [1, 2, 3, 4, 5, 8, 9, 10]
min_num, second_min_num, max_index = find_min_max(numbers)
print("Phần tử nhỏ nhất là", min_num)
print("Phần tử nhỏ thứ hai là", second_min_num)
print("Vị trí của phần tử lớn nhất là", max_index)
