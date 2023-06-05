Để giải quyết bài toán này, ta có thể sử dụng thuật toán tham lam (greedy algorithm) để sắp xếp các con kiến và tạo các nhóm đi qua cành cây.

Bước 1: Đọc dữ liệu từ file GROUANTS.INP

Bước 2: Sắp xếp các con kiến theo thứ tự tăng dần của vận tốc di chuyển.

Bước 3: Tạo các nhóm và tính thời gian đi của mỗi nhóm:

Khởi tạo biến nhóm = 0 (số nhóm ban đầu là 0)
Khởi tạo biến tổng khối lượng = 0 (tổng khối lượng của các con kiến trong một nhóm)
Khởi tạo biến thời gian = 0 (tổng thời gian đi qua cành cây)
Duyệt qua từng con kiến:
Nếu (tổng khối lượng + khối lượng con kiến) <= m (khối lượng tối đa cho phép trong một nhóm):
Tổng khối lượng = tổng khối lượng + khối lượng con kiến
Thời gian = thời gian + (khối lượng con kiến / vận tốc con kiến)
Ngược lại:
Tăng số nhóm lên 1
Gán tổng khối lượng bằng khối lượng con kiến
Thời gian = thời gian + (khối lượng con kiến / vận tốc con kiến)
Ghi tổng thời gian vào file GROUANTS.OUT
Bước 4: Kết thúc.