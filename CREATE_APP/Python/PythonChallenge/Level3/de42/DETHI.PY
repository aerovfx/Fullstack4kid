from itertools import combinations #Dòng này import hàm combinations từ module itertools. Hàm này sẽ được sử dụng để tạo ra tất cả các tổ hợp có thể từ danh sách các số.

def count_combinations(n, k, numbers): # Định nghĩa hàm count_combinations nhận đầu vào là n, k và numbers. Hàm này sẽ tính toán tất cả các tổ hợp có thể và trả về kết quả dưới dạng tập hợp (set) các tổ hợp.
    combinations = set()

    def find_combinations(target, current_combination, visited): #Định nghĩa hàm đệ quy find_combinations nhận các tham số target, current_combination và visited. Hàm này tìm các tổ hợp có tổng độ khó là target và có đúng k phần tử. Trong trường hợp tổ hợp hợp lệ, nó được thêm vào tập hợp combinations.
        if target == 0 and len(current_combination) == k:
            sorted_combination = tuple(sorted(current_combination))
            combinations.add(sorted_combination)
            return

        if target < 0 or len(current_combination) > k:
            return

        for i in range(len(numbers)): # Vòng lặp for duyệt qua danh sách numbers để chọn các số chưa được thăm. Nếu số đó chưa được thăm, nó sẽ được thêm vào current_combination. Hàm find_combinations được gọi đệ quy với remaining (tổng còn lại sau khi chọn số), current_combination đã cập nhật và visited đã được đánh dấu. Sau khi quay lui, visited sẽ được đánh dấu lại là False để tiếp tục tìm kiếm các tổ hợp khác.
            if not visited[i]:
                visited[i] = True
                remaining = target - numbers[i]
                find_combinations(remaining, current_combination + [numbers[i]], visited)
                visited[i] = False

    visited = [False] * len(numbers) # Mảng visited được khởi tạo với giá trị False cho mỗi số từ 1 đến n. Sau đó, hàm find_combinations được gọi để tìm các tổ hợp khác nhau.
    find_combinations(n, [], visited)

    return combinations # Kết quả là tập hợp (set) các tổ hợp combinations.

with open('DETHI.INP', 'r') as f: # Mở tệp "DETHI.INP" để đọc dữ liệu. n và k được đọc từ dòng đầu tiên của tệp. numbers được khởi tạo là danh sách các số từ 1 đến n.
    n, k = map(int, f.readline().split())
    numbers = list(range(1, n + 1))

dethi = count_combinations(n, k, numbers)
count = len(dethi) # Gọi hàm count_combinations để tính toán tất cả các tổ hợp có thể và lưu kết quả vào biến dethi. count lưu trữ số lượng tổ hợp trong dethi.
 
with open('DETHI.OUT', 'w') as f: # Mở tệp "DETHI.OUT" để ghi kết quả. Đầu tiên, số lượng tổ hợp (count) được ghi vào dòng đầu tiên của tệp. Sau đó, từng tổ hợp trong dethi được ghi vào các dòng tiếp theo, mỗi tổ hợp được viết dưới dạng các số cách nhau bởi dấu cách.
    f.write(str(count) + '\n')
    for combination in dethi:
        f.write(' '.join(map(str, combination)) + '\n')
