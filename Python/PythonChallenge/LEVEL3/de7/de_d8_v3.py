'''Trong chương trình này:

Chúng ta định nghĩa một hàm is_prime(num) để kiểm tra xem một số có phải là số nguyên tố hay không.
Chương trình mở tệp "NGUYENTO.INP" để đọc dữ liệu, bao gồm số lượng phần tử n và dãy số data.
Chương trình sử dụng một từ điển primes để đếm số lượng số nguyên tố xuất hiện và tìm số nguyên tố xuất hiện nhiều nhất.
Kết quả được ghi vào tệp "NGUYENTO.OUT", nếu không tìm thấy số nguyên tố nào, chương trình sẽ ghi "Khong tim duoc gia tri" vào tệp.

NGUYENTO.INP
5
2 3 5 7 11'''
from math import sqrt

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

try:
    # Mở tệp đầu vào để đọc
    with open("NGUYENTO.INP", "r") as input_file:
        n = int(input_file.readline())  # Đọc số lượng phần tử
        data = list(map(int, input_file.readline().split()))  # Đọc dãy số

    # Đếm số lượng số nguyên tố và tìm số nguyên tố xuất hiện nhiều nhất
    primes = {}
    max_count = 0
    max_prime = None
    for num in data:
        if is_prime(num):
            if num in primes:
                primes[num] += 1
            else:
                primes[num] = 1
            if primes[num] > max_count:
                max_count = primes[num]
                max_prime = num

    # Mở tệp đầu ra để ghi
    with open("NGUYENTO.OUT", "w") as output_file:
        if max_prime is None:
            output_file.write("Khong tim duoc gia tri")
        else:
            output_file.write(f"{max_prime} {max_count}")

except FileNotFoundError:
    print("File not found: NGUYENTO.INP")
except ValueError:
    print("Invalid data in the file")
except IOError:
    print("Error reading or writing file")