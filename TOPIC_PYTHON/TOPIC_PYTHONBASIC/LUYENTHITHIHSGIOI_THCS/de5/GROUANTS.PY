def find_minimum_time(n, m, l, kiens):
    groups = []  # Danh sách các nhóm kiến
    group = []  # Nhóm hiện tại
    total_weight = 0  # Khối lượng tổng của nhóm hiện tại

    for i in range(n):
        weight, speed = kiens[i]

        # Nếu khối lượng tổng và vận tốc của con kiến hiện tại không phù hợp với nhóm hiện tại
        if total_weight + weight > m:
            groups.append(group)  # Thêm nhóm hiện tại vào danh sách các nhóm
            group = []  # Tạo nhóm mới
            total_weight = 0  # Reset khối lượng tổng

        group.append(kiens[i])  # Thêm con kiến vào nhóm hiện tại
        total_weight += weight  # Cập nhật khối lượng tổng của nhóm

    if group:
        groups.append(group)  # Thêm nhóm cuối cùng vào danh sách các nhóm

    min_time = 0  # Tổng thời gian đi của các nhóm
    for group in groups:
        min_speed = min(group, key=lambda x: x[1])[1]  # Tìm vận tốc nhỏ nhất trong nhóm
        time = l / min_speed  # Tính thời gian đi của nhóm (quãng đường l chia cho vận tốc nhỏ nhất)
        min_time += time

    return min_time


# Đọc dữ liệu từ file
with open("GROUANTS.INP", "r") as file:
    n, m, l = map(int, file.readline().split())
    kiens = [list(map(int, line.split())) for line in file]

# Tính thời gian nhỏ nhất
tong_thoi_gian = find_minimum_time(n, m, l, kiens)

# Ghi kết quả vào file
with open("GROUANTS.OUT", "w") as file:
    file.write(str(tong_thoi_gian))
