def solve():
    # Bước 1: Đọc dữ liệu từ file GROUANTS.INP
    with open('GROUANTS.INP', 'r') as f:
        n, m, l = map(int, f.readline().split())
        ants = []
        for _ in range(n):
            k, v = map(int, f.readline().split())
            ants.append((k, v))

    # Bước 2: Sắp xếp các con kiến theo thứ tự tăng dần của vận tốc di chuyển
    ants.sort(key=lambda x: x[1])

    # Bước 3: Tạo các nhóm và tính thời gian đi của mỗi nhóm
    group = 0
    total_weight = 0
    total_time = 0

    for i in range(n):
        weight, speed = ants[i]
        if total_weight + weight <= m:
            total_weight += weight
            total_time += weight / speed
        else:
            group += 1
            total_weight = weight
            total_time += weight / speed

    # Bước 4: Ghi tổng thời gian vào file GROUANTS.OUT
    with open('GROUANTS.OUT', 'w') as f:
        f.write("{:.2f}".format(total_time))

# Gọi hàm solve để thực hiện giải quyết bài toán
solve()
