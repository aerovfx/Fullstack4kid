# Đọc dữ liệu từ file GROUANTS.INP
with open('GROUANTS.INP', 'r') as f:
    lines = f.readlines()
    n, m, l = map(int, lines[0].split())
    ants = [list(map(int, line.split())) for line in lines[1:]]

# Tính thời gian nhỏ nhất
def tinh_thoi_gian_nho_nhat(n, m, l, ants):
    # ... (phần code tính thời gian nhỏ nhất giữ nguyên)

# Gọi hàm tính thời gian nhỏ nhất
thoi_gian_nho_nhat = tinh_thoi_gian_nho_nhat(n, m, l, ants)

# Ghi kết quả vào file GROUANTS.OUT
with open('GROUANTS.OUT', 'w') as f:
    f.write(str(thoi_gian_nho_nhat))
