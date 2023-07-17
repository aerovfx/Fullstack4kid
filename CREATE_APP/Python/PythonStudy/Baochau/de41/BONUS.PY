def timphanthuongtoida(m, n, w, h, a, b):
    # tạo ma trận tổng tích luỹ
    tongtiento = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            tongtiento[i][j] = tongtiento[i][j - 1] + tongtiento[i-1][j] - tongtiento[i-1][j-1] + a[i-1] + b[j-1] 
    phanthuong_toida = 0
    
    # duyệt qa all các khung hình có kích thước w*h
    for i in range(m - w +1):
        for j in range(n - h + 1):
            # tính tổng giá trị của khung hình hiện tại
            phanthuong = tongtiento[i + w][j + h] - tongtiento[i + w][j] - tongtiento[i][j+h] + tongtiento[i][j]
            phanthuong_toida = max(phanthuong_toida, phanthuong)
    return phanthuong_toida

# đọc dữ liệu
with open('BONUS.INP', 'r') as file:
    m, n, w, h = map(int, file.readline().split())
    a = list(map(int, file.readline().split()))
    b = list(map(int, file.readline().split()))
    
# gọi hàm tìm giá trị lớn nhất và lưu két quả vào file
phanthuong_lonnhat = timphanthuongtoida(m, n, w, h, a, b)
with open('BONUS.OUT', 'w') as file:
    file.write(str(phanthuong_lonnhat))