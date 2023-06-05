# Đọc dữ liệu từ file GROUANTS.INP
n, m, l = map(int, input().split())
kien_info = []
for _ in range(n):
    k, v = map(int, input().split())
    kien_info.append((k, v))

# Sắp xếp các con kiến theo thứ tự tăng dần của vận tốc di chuyển
kien_info.sort(key=lambda x: x[1])

# Khởi tạo biến tổng thời gian và khối lượng hiện tại trên cành cây
tong_thoi_gian = 0
khoi_luong_hien_tai = 0

# Duyệt qua từng con kiến theo thứ tự đã sắp xếp
for i in range(n):
    k, v = kien_info[i]
    
    # Nếu (khối lượng hiện tại + khối lượng của con kiến) <= m
    if (khoi_luong_hien_tai + k) <= m:
        # Cộng dồn khối lượng của con kiến vào khoi_luong_hien_tai
        khoi_luong_hien_tai += k
        
        # Tính thời gian đi qua cành cây của nhóm hiện tại
        thoi_gian = khoi_luong_hien_tai / v
        
        # Cập nhật tổng thời gian
        tong_thoi_gian += thoi_gian
    else:
        # Tính thời gian đi qua cành cây của nhóm hiện tại
        thoi_gian = khoi_luong_hien_tai / v
        
        # Cập nhật tổng thời gian
        tong_thoi_gian += thoi_gian
        
        # Gán khối lượng hiện tại bằng khối lượng của con kiến
        khoi_luong_hien_tai = k

# In ra màn hình kết quả
print("Thời gian nhỏ nhất là:", format(tong_thoi_gian, ".2f"))

# Ghi kết quả vào file GROUANTS.OUT
with open("GROUANTS.OUT", "w") as f:
    f.write(format(tong_thoi_gian, ".2f"))

