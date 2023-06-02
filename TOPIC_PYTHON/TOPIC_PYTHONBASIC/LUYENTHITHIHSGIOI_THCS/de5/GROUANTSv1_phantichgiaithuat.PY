# Dữ liệu đầu vào
n = 6
m = 10
l = 10
ants = [
    [3, 5],
    [6, 2],
    [5, 2],
    [7, 1],
    [1, 5],
    [2, 7]
]

# Tính tổng khối lượng của từng nhóm kiến
nhom1_khoi_luong = ants[0][0] + ants[1][0]
nhom2_khoi_luong = ants[2][0]
nhom3_khoi_luong = ants[3][0] + ants[4][0] + ants[5][0]

# Tính thời gian đi qua cành cây của từng nhóm
nhom1_thoi_gian = m / min(ants[0][1], ants[1][1])
nhom2_thoi_gian = m / ants[2][1]
nhom3_thoi_gian = l / min(ants[3][1], ants[4][1], ants[5][1])

# Tính tổng thời gian nhỏ nhất
tong_thoi_gian = nhom1_thoi_gian + nhom2_thoi_gian + nhom3_thoi_gian

# In ra màn hình kết quả
print("Thời gian nhỏ nhất là:", tong_thoi_gian)
