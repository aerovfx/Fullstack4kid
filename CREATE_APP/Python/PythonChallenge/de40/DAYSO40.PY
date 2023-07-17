n = int(input('nhập số lượng phần tử của dãy số A: '))
        
# đọc n phần tử của dãy số A từ bàn phím
A = list(map(int,input('nhập dãy só A, các phần tử cách nhau dấu cách : ').split()))
# tạo bảng Dp kích thước n*n
DP = [[0]*n for _ in range(n)]
# khởi tạo DP[i][i] = 1 cho mọi i từ 0 đến n-1
for i in range(n):
    DP[i][i] = 1
    
# khởi tạo biến max_len là độ dài của dãy số con đối xứng dài nhất tìm đc
max_len = 1

start = 0
end = 0

# duyệt i từ n-1 đến 0 và từ j đến n -1
for i in range(n-1,-1, -1):
    for j in range(i+1,n):
        if A[i] == A[j] and j-i +1> DP[i+1][j-1]:
            DP[i][j] = DP[i+1][j-1]+2
            if DP[i][j] > max_len:
                max_len = DP[i][j]
                start = i
                end = j
                
# in dãy số con đối xứng dài nhất từ start dến end trong dãy A
print('dãy số con đối xứng dài nhất của dãy A là : ', A[start:end+1])