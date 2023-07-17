def count_unsupplied_locations(n, data):
    data.sort(key=lambda x: x[0])  # Sắp xếp dữ liệu theo vị trí x_i

    max_position = 0  # Vị trí cung cấp khẩu trang cuối cùng
    count = 0  # Số điểm chưa được cung cấp khẩu trang

    for i in range(n):
        position, radius = data[i]
        
        if position > max_position:
            count += position - max_position - 1
            max_position = position + radius
        elif position + radius > max_position:
            max_position = position + radius

    return count

# Đọc dữ liệu từ tệp tin đầu vào
with open('KHAUTRANG.INP', 'r') as file:
    lines = file.readlines()
    n = int(lines[0].strip())
    data = []
    for line in lines[1:]:
        x, r = map(float, line.strip().split())
        data.append((x, r))

# Tính toán số điểm chưa được cung cấp khẩu trang
result = count_unsupplied_locations(n, data)

# Ghi kết quả vào tệp tin đầu ra
with open('KHAUTRANG.OUT', 'w') as file:
    file.write(str(result))