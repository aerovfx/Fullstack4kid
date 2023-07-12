def maxBonusValue(m, n, w, h, a, b):
    # Tạo ma trận dp với kích thước (m+1)x(n+1) và khởi tạo giá trị ban đầu là 0
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    # Duyệt qua từng ô của ma trận dp và tính giá trị tối đa
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Tính tổng giá trị của bảng con kích thước wxh, có gốc tại ô (i, j)
            total = 0
            for x in range(i, i+ w):
                for y in range(j, j+ h):
                    if x <= m and y <= n:  # Kiểm tra phạm vi của x và y
                        total += a[x-1] + b[y-1]
            # Cập nhật giá trị tối đa cho ô (i, j)
            dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] + total)
    
    return dp[m][n]

# Đọc dữ liệu từ file
with open("BONUS.INP", "r") as file:
    m, n, w, h = map(int, file.readline().strip().split())  # Đọc các giá trị m, n, w, h
    a = list(map(int, file.readline().strip().split()))  # Đọc danh sách giá trị a
    b = list(map(int, file.readline().strip().split()))  # Đọc danh sách giá trị b

# Tính tổng giá trị lớn nhất mà An có thể nhận được
result = maxBonusValue(m, n, w, h, a, b)

# Ghi kết quả vào file
with open("BONUS.OUT", "w") as file:
    file.write(str(result))  # Ghi kết quả vào file "BONUS.OUT"
