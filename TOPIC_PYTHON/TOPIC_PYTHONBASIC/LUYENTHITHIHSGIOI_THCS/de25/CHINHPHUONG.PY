import math

# Đọc dữ liệu từ file input
with open('CHINHPHUONG.INP', 'r') as input_file:
    N = int(input_file.readline())
    A = list(map(int, input_file.readline().split()))

# Tìm số chính phương nhỏ nhất
P = 1
for i in range(N):
    P = P * A[i] // math.gcd(P, A[i])
    print(P) #Check kết qủa của P trong vòng lặp.
# Tính phần dư của phép chia P cho 10^9 + 7
result = P**2 % (10**9 + 7)

# Ghi kết quả vào file output
with open('CHINHPHUONG.OUT', 'w') as output_file:
    output_file.write(str(result))
