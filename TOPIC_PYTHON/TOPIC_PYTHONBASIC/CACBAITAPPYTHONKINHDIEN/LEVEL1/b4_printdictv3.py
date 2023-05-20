# Đọc dữ liệu từ file INPUT
with open("b4_DICT.INP", "r") as file:
    numbers = file.readlines()

# Tạo từ điển chứa (i, i*i) từ 1 đến n
results = {}
for num in numbers:
    n = int(num.strip())
    result = {i: i*i for i in range(1, n+1)}
    results[n] = result

# Xuất kết quả vào file OUTPUT
with open("b4_DICT.OUT", "w") as file:
    for n, result in results.items():
        file.write(f"{n} thì đầu ra {result}\n")
