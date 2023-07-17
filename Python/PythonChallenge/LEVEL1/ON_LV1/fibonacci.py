def fibonacci(n):
    fibo_list = [1,1] # Khởi tạo dãy Fibonacci với hai số đầu tiên là 0 và 1
    while len(fibo_list)<n:
        result = fibo_list[-1] + fibo_list[-2]  # Tính số Fibonacci tiếp theo
        fibo_list.append(result)
    return fibo_list

n = int(input('nhap so: '))
fibo_sequence = fibonacci(n)
print('day fibonacci co',n,'so dau tien la:')
for num in fibo_sequence:
    print(num)
