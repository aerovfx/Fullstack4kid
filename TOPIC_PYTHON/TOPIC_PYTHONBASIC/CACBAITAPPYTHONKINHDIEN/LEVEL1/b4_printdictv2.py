# Đọc dữ liệu từ file INPUT
with open("b4_DICT.INP", "r") as file:
    n = int(file.read().strip())

# Tạo từ điển chứa (i, i*i) từ 1 đến n
d = {}
for i in range(1, n + 1):
    d[i] = i * i

# Xuất kết quả vào file OUTPUT
with open("b4_DICT.OUT", "w") as file:
    file.write("{\n")
    for key, value in d.items():
        file.write(f"  {key}: {value},\n")
    file.write("}\n")
