def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_prime_numbers(A, B):
    prime_numbers = []
    prime_sum = 0

    for num in range(A, B + 1):
        if is_prime(num):
            prime_numbers.append(num)
            prime_sum += num

    return prime_numbers, prime_sum


# Đọc dữ liệu từ file input
with open('SUMPRIME.INP', 'r') as input_file:
    A, B = map(int, input_file.readline().split())

# Tính tổng các số nguyên tố và lưu vào biến result
prime_numbers, prime_sum = sum_prime_numbers(A, B)

# Ghi kết quả vào file output
with open('SUMPRIME.OUT', 'w') as output_file:
    output_file.write("Dãy số nguyên tố:\n")
    output_file.write(" ".join(str(num) for num in prime_numbers))
    output_file.write("\nTổng của dãy số nguyên tố: ")
    output_file.write(str(prime_sum))
