def find_minimum_time(n, m, l, kiens):
    groups = []
    total_weight = 0
    total_time = 0

    for i in range(n):
        k_i, v_i = kiens[i]
        if total_weight + k_i <= m:  # Kiểm tra khối lượng của nhóm hiện tại
            total_weight += k_i
            if i == 0 or v_i != kiens[i - 1][1]:
                groups.append([i + 1])
            else:
                groups[-1].append(i + 1)

    for group in groups:
        group_weight = sum(kiens[i - 1][0] for i in group)  # Tính tổng khối lượng của nhóm
        group_time = l / min(kiens[i - 1][1] for i in group)  # Tính thời gian đi của mỗi nhóm
        total_time += group_time

    with open('GROUANTS.OUT', 'w') as f:
        f.write(f"{total_time:.2f}")


# Đọc dữ liệu từ file GROUANTS.INP
with open('GROUANTS.INP', 'r') as f:
    n, m, l = map(int, f.readline().split())
    kiens = [list(map(int, line.split())) for line in f]

# Gọi hàm để tìm tổng thời gian nhỏ nhất
find_minimum_time(n, m, l, kiens)
