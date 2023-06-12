def tinh_thoi_gian_di(n, m, l, kiens):
    #Sắp xếp các kiến theo khối lượng giảm dần
    #kiens.sort(reverse=True)
    
    tong_thoi_gian = 0  # Tổng thời gian đi qua cành cây
    tong_khoi_luong = 0  # Tổng khối lượng của nhóm kiến
    
    for kien in kiens:
        khoi_luong, van_toc = kien
        
        # Kiểm tra xem có thể thêm kiến vào nhóm hiện tại hay không
        if tong_khoi_luong + khoi_luong <= m:
            tong_khoi_luong += khoi_luong
        else:
            # Cần tạo nhóm mới vì khối lượng đã vượt quá tải trọng
            tong_thoi_gian += l / min(van_toc, kiens[0][1])
            tong_khoi_luong = khoi_luong
        
        # Tính thời gian đi qua cành cây cho nhóm hiện tại
        tong_thoi_gian += l / min(van_toc, kiens[0][1])
    
    return tong_thoi_gian

# Đọc dữ liệu từ file INPUT
with open("GROUANTS.INP", "r") as file:
    n, m, l = map(int, file.readline().strip().split())
    kiens = []
    for _ in range(n):
        khoi_luong, van_toc = map(int, file.readline().strip().split())
        kiens.append((khoi_luong, van_toc))

# Tính tổng thời gian nhỏ nhất
tong_thoi_gian = tinh_thoi_gian_di(n, m, l, kiens)

# Ghi kết quả vào file OUTPUT
with open("GROUANTS.OUT", "w") as file:
    file.write("{:.2f}".format(tong_thoi_gian))
