def fibonacci_numbers(n):
    fib_numbers = [1, 1]  # Khởi tạo danh sách số Fibonacci với hai số đầu tiên là 1

    for i in range(2, n):
        fib_num = fib_numbers[i - 1] + fib_numbers[i - 2]
        fib_numbers.append(fib_num)

    return fib_numbers


# In ra n số Fibonacci đầu tiên
n = int(input("Nhập số n: "))
fibonacci_nums = fibonacci_numbers(n)
print(f"N số Fibonacci đầu tiên là: {fibonacci_nums}")

# In ra các số Fibonacci nhỏ hơn hoặc bằng n
n = int(input("Nhập số n: "))
fibonacci_nums = []
a, b = 1, 1
while a <= n:
    fibonacci_nums.append(a)
    a, b = b, a + b

print(f"Các số Fibonacci nhỏ hơn hoặc bằng {n} là: {fibonacci_nums}")
