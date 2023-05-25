def count_continuous_subsequences(n, S, A):
    count = 0
    prefix_sum = 0
    prefix_sum_count = {0: 1}

    for i in range(n):
        prefix_sum += A[i]

        if prefix_sum >= S:
            count += prefix_sum_count.get(prefix_sum - S, 0)

        abs_prefix_sum = abs(prefix_sum)

        for j in range(1, abs_prefix_sum + 1):
            if (abs_prefix_sum - j) in prefix_sum_count:
                count += prefix_sum_count[abs_prefix_sum - j]

        prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum, 0) + 1

    return count


# Đọc dữ liệu từ file
with open('CNTSEQ.INP', 'r') as file:
    n, S = map(int, file.readline().split())
    A = list(map(int, file.readline().split()))

# Đếm số dãy con liên tiếp thỏa mãn yêu cầu
result = count_continuous_subsequences(n, S, A)

# Ghi kết quả vào file đầu ra
with open('CNTSEQ.OUT', 'w') as file:
    file.write(str(result))
