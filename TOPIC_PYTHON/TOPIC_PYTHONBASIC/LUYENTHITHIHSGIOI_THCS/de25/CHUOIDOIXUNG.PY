def is_palindrome(string):
    reversed_string = string[::-1]  # Chuỗi đảo ngược
# [::-1] là cú pháp slicing của Python để chỉ định các bước nhảy và hướng.
# Trong trường hợp này, [::-1] có nghĩa là lấy toàn bộ chuỗi từ đầu đến cuối, 
# nhưng theo hướng ngược lại. Bước nhảy là -1, điều này làm cho các phần tử được lấy theo thứ tự ngược lại.
    if string == reversed_string:
        return True
    else:
        return False

# Nhập chuỗi từ người dùng
input_string = input("Nhập chuỗi ký tự: ")

# Kiểm tra đối xứng và in kết quả
if is_palindrome(input_string):
    print("Chuỗi là đối xứng")
else:
    print("Chuỗi không phải là đối xứng")
