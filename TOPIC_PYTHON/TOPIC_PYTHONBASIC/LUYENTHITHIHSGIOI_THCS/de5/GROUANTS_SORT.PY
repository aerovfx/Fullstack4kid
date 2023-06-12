def find_minimum_time(n, m, l, kiens):
    kiens.sort(key=lambda x: x[1])  # Sắp xếp các kiến theo vận tốc tăng dần
    groups = []
    total_weight = 0
    total_time = 0

    for i in range(n):
        k_i, v_i = kiens[i]
        if total_weight + k_i <= m:  # Kiểm tra khối lượng của nhóm hiện tại
            total_weight += k_i
            if i == 0 or v_i != kiens[i-1][1]:
                groups.append([i + 1])
            else:
                groups[-1].append(i + 1)
        else:
            break

    for group in groups:
        max_v = kiens[group[0] - 1][1]
        group_time = sum([kiens[kien - 1][0] for kien in group]) / max_v
        total_time += group_time

    with open('GROUANTS.OUT', 'w') as f:
        f.write(f"{total_time:.2f}")


# Đọc dữ liệu từ file GROUANTS.INP
with open('GROUANTS.INP', 'r') as f:
    n, m, l = map(int, f.readline().split())
    kiens = [list(map(int, line.split())) for line in f]

# Gọi hàm để tìm tổng thời gian nhỏ nhất
find_minimum_time(n, m, l, kiens)
