def find_positive_even_numbers(numbers):
    count = 0
    for num in numbers:
        if num > 0 and num % 2 == 0:
            count += 1
    return count

def find_max_negative(numbers):
    max_negative = None
    indices = []
    for i, num in enumerate(numbers):
        if num < 0:
            if max_negative is None or num > max_negative:
                max_negative = num
                indices = [i]
            elif num == max_negative:
                indices.append(i)
    return indices

def find_longest_sequences(numbers):
    sequences = []
    current_sequence = []
    for num in numbers:
        if num != 0 and (not current_sequence or current_sequence[-1] * num > 0):
            current_sequence.append(num)
        else:
            if current_sequence:
                sequences.append(current_sequence)
            current_sequence = []
    if current_sequence:
        sequences.append(current_sequence)
    max_length = max(len(seq) for seq in sequences)
    longest_sequences = [seq for seq in sequences if len(seq) == max_length]
    return longest_sequences

# Nhập số N từ bàn phím
N = int(input("Nhập số N: "))

# Nhập dãy N số nguyên từ bàn phím
numbers = []
for i in range(N):
    num = int(input(f"Nhập số thứ {i + 1}: "))
    numbers.append(num)

# Tìm số dương chẵn trong dãy
positive_even_count = find_positive_even_numbers(numbers)

# Tìm chỉ số của giá trị âm lớn nhất
max_negative_indices = find_max_negative(numbers)

# Tìm tất cả các dãy con dài nhất các số khác không cùng dấu
longest_sequences = find_longest_sequences(numbers)

# In kết quả
print("Số dương chẵn trong dãy:", positive_even_count)
print("Chỉ số của giá trị âm lớn nhất:", max_negative_indices)
print("Tất cả các dãy con dài nhất các số khác không cùng dấu:")
for seq in longest_sequences:
    print(seq)
