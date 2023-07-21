def bieuthuc(n, x, y):
    result = 0
    for i in range(2, n + 1):
        result += x ** i + y / i
    return result

# Đọc dữ liệu từ file "DAYSO.INP"
with open("BAI6.INP", "r") as file:
    n = int(file.readline())
    x, y = map(int, file.readline().split())

# In ra kết quả
result = (bieuthuc(n, x, y))
with open("BAI6.OUT", "w") as file:
    file.write(str(result))