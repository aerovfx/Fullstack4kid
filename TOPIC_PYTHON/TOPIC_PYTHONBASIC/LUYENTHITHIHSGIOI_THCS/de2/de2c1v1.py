n = 5
q = 2
a = [1, 2, 8, 4, 2]

for k in range(2, 6):
    count = 0  # Biến đếm số lượng dãy con cấp số nhân công bội với q
    for i in range(n - k + 1):
        subsequence = a[i:i+k]  # Lấy dãy con từ a[i] đến a[i+k-1]
        is_geometric = True  # Biến kiểm tra dãy con có phải là cấp số nhân công bội không

        for j in range(1, k):
            if subsequence[j] % subsequence[j - 1] != 0 or subsequence[j] / subsequence[j - 1] != q:
                is_geometric = False
                break

        if is_geometric:
            count += 1

    print(count, end=' ')