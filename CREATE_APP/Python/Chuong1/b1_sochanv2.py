numbers = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = numbers.split(",")  # Tách danh sách thành các số

even_numbers = []
odd_numbers = []

for num in numbers:
    num = int(num)
    if num % 2 == 0:
        even_numbers.append(str(num))
    else:
        odd_numbers.append(str(num))

print("Các số chẵn: " , ", ".join(even_numbers))
print("Các số lẻ: " , ", ".join(odd_numbers))
