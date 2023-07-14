def xauchuoidainhat(s1, s2):
    m = len(s1)
    n = len(s2)
    
    # tạo bảng lưu trữ độ dài xâu con chung dài nhát
    #tại vị trí (i, j) trong bảng lưu trữ, giá trị độ dài của xâu con chung của s1 và s2 )
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    # tạo biến lư trữ đọ dài xâu con chung dài nhất
    max_len = 0
   
    # vị trí kết thúc xâu con chung dài nhát
    end_pos = 0
    
    # lập qa các phàn tử
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_pos = i

    # trích xuất xâu con chung
    long_subsstring = s1[end_pos - max_len: end_pos]
    return long_subsstring

# nhập s1 và s2
s1 = input('nhập vào xâu s1: ')
s2 = input('nhập vào xâu s2: ')

# tìm xâu con chung dài nhất
result = xauchuoidainhat(s1, s2)
# in kq
print('xâu con chung dài nhất là: ',result)