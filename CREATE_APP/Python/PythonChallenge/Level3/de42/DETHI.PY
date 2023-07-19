from itertools import combinations

def count_combinations(n, k, numbers):
    combinations = set()  # Tạo một tập hợp rỗng để lưu trữ các tổ hợp

    def find_combinations(target, current_combination, visited):
        if target == 0 and len(current_combination) == k:
            sorted_combination = tuple(sorted(current_combination))  # Sắp xếp tổ hợp để đảm bảo tính duy nhất
            combinations.add(sorted_combination)  # Thêm tổ hợp vào tập hợp
            return

        if target < 0 or len(current_combination) > k:
            return  # Không tìm thấy tổ hợp hợp lệ, thoát hàm

        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True  # Đánh dấu số đã được chọn
                remaining = target - numbers[i]  # Tính tổng còn lại sau khi chọn số
                find_combinations(remaining, current_combination + [numbers[i]], visited)  # Gọi đệ quy với số tiếp theo
                visited[i] = False  # Bỏ đánh dấu số đã được chọn để thử các tổ hợp khác

    visited = [False] * len(numbers)  # Tạo một mảng gồm các giá trị False để theo dõi các số đã được chọn
    find_combinations(n, [], visited)  # Gọi hàm đệ quy để tìm các tổ hợp

    return combinations  # Trả về tập hợp các tổ hợp

with open('DETHI.INP', 'r') as f:
    n, k = map(int, f.readline().split())  # Đọc dữ liệu từ tệp input
    numbers = list(range(1, n + 1))  # Tạo danh sách các số từ 1 đến n

dethi = count_combinations(n, k, numbers)  # Gọi hàm để tính toán các tổ hợp
count = len(dethi)  # Đếm số lượng tổ hợp

with open('DETHI.OUT', 'w') as f:
    f.write(str(count) + '\n')  # Ghi số lượng tổ hợp vào tệp output
    for combination in dethi:
        f.write(' '.join(map(str, combination)) + '\n')  # Ghi từng tổ hợp vào tệp output
