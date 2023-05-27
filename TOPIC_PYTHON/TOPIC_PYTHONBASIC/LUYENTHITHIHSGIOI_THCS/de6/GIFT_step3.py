def choose_gifts(gifts, curr_idx, curr_value, k, chosen_gifts):
    global max_gifts

    # Kiểm tra điều kiện dừng
    if curr_idx >= len(gifts):
        # Nếu số lượng phần quà được chọn vượt quá max_gifts, cập nhật max_gifts và danh sách phần quà được chọn
        if len(chosen_gifts) > max_gifts:
            max_gifts = len(chosen_gifts)
            chosen_gifts_copy = chosen_gifts.copy()
            all_chosen_gifts.append(chosen_gifts_copy)
        return

    # Chọn phần quà hiện tại
    if curr_value <= gifts[curr_idx]:
        chosen_gifts.append(gifts[curr_idx])
        choose_gifts(gifts, curr_idx + 1, gifts[curr_idx], k, chosen_gifts)
        chosen_gifts.pop()

    # Không chọn phần quà hiện tại
    if max_gifts + len(gifts) - curr_idx > k:
        choose_gifts(gifts, curr_idx + 1, curr_value, k, chosen_gifts)


# Dữ liệu đầu vào
N = 5
K = 2
A = [4, 5, 6, 4, 8]

max_gifts = 0
chosen_gifts = []
all_chosen_gifts = []
choose_gifts(A, 0, 0, K, chosen_gifts)

# In kết quả
print("Số lượng phần quà được chọn nhiều nhất:", max_gifts)
print("Các lựa chọn:")
for chosen_gifts in all_chosen_gifts:
    print(chosen_gifts)
