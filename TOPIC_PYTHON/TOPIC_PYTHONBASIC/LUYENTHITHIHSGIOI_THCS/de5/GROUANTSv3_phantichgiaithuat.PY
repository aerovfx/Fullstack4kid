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

# Sắp xếp danh sách nhóm kiến theo thứ tự giảm dần của vận tốc
sorted_ants = sorted(ants, key=lambda x: x[1], reverse=True)

# Khởi tạo danh sách kết quả
result = []

# Duyệt qua từng nhóm kiến
for ant in sorted_ants:
    if sum([x[0] for x in result]) + ant[0] <= m:
        result.append(ant)

# Tính thời gian đi qua cành cây
total_time = l / max([x[1] for x in result])

# In ra kết quả thời gian nhỏ nhất
print("Thời gian nhỏ nhất là:", total_time)
