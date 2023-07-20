with open("MARATHON.INP", "r") as input_file:
    n = int(input_file.readline())  # Đọc số lượng đoàn viên từ dòng đầu tiên của tệp
    times = list(map(int, input_file.readline().split()))  # Đọc thời gian chạy của từng đoàn viên từ dòng thứ hai và chuyển thành danh sách

result = []  # Khởi tạo danh sách kết quả

# Duyệt qua từng đoàn viên
for i in range(n):
    count = 1  # Đặt giá trị ban đầu của số lượng đoàn viên được trao thưởng là 1

    # Kiểm tra từng đoàn viên khác
    for j in range(n):
        if times[j] <= times[i]:  # Nếu thời gian chạy của đoàn viên khác nhỏ hơn hoặc bằng thời gian chạy của đoàn viên hiện tại
            count += 1  # Tăng số lượng đoàn viên được trao thưởng lên 1

    result.append(count)  # Thêm số lượng đoàn viên được trao thưởng cho đoàn viên hiện tại vào danh sách kết quả

with open("MARATHON.OUT", "w") as output_file:
    for count in result:
        output_file.write(str(count) + "\n")  # Ghi số lượng đoàn viên được trao thưởng cho từng đoàn viên vào tệp kết quả, mỗi giá trị trên một dòng
