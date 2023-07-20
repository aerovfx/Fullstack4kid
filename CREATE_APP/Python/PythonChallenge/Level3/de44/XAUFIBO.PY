def is_fibonacci(string): # Hàm kiểm tra dãy fibonacci
    n = len(string)

    if n < 3:
        return False  # Xâu có ít hơn 3 phần tử không thể là chuỗi Fibonacci

    fib = [0, 1]
    while len(str(fib[-1])) < n:
        fib.append(fib[-1] + fib[-2])  # Xây dựng danh sách các số Fibonacci cho đến khi số cuối cùng có độ dài tương đương xâu đầu vào

    if string[:n] != str(fib[-1]):
        return False  # Xâu không bắt đầu bằng số Fibonacci cuối cùng, không thể là chuỗi Fibonacci

    for i in range(2, n // 2 + 1):
        a = int(string[:i])
        b = int(string[i:i*2])
        temp = str(a + b)
        if string[i*2:i*2+len(temp)] != temp:
            return False  # Xâu không tuân theo quy tắc Fibonacci, không phải là chuỗi Fibonacci

    return True  # Xâu qua tất cả các kiểm tra, là chuỗi Fibonacci

input_string = input("Nhập xâu: ")

if is_fibonacci(input_string):
    print("Xâu là chuỗi Fibonacci.")
else:
    print("Xâu không phải là chuỗi Fibonacci.")
