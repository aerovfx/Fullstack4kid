def find_next_permutation(s):
    n = len(s)

    # Tìm vị trí i sao cho s[i] < s[i+1]
    i = n - 2
    while i >= 0 and s[i] >= s[i+1]:
        i -= 1

    # Nếu không tìm thấy, tức là s đã là xâu lớn nhất
    if i == -1:
        return s

    # Tìm vị trí j sao cho s[j] là số nhỏ nhất lớn hơn s[i]
    j = n - 1
    while s[j] <= s[i]:
        j -= 1

    # Hoán đổi s[i] và s[j]
    s[i], s[j] = s[j], s[i]

    # Đảo ngược đoạn cuối cùng của xâu
    left = i + 1
    right = n - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return s


# Đọc dữ liệu vào từ file XAU42.INP
with open('XAU42.INP', 'r') as f:
    s = list(f.readline().strip())

# Tìm xâu S1
s1 = find_next_permutation(s)

# Ghi kết quả vào file XAU42.OUT
with open('XAU42.OUT', 'w') as f:
    f.write(''.join(s1))
