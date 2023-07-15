def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True

# Nhập danh sách từ người dùng
nums = input("Nhập danh sách các số nguyên, cách nhau bởi dấu cách: ").split()
nums = [int(num) for num in nums]

# Kiểm tra và in kết quả
if is_sorted(nums):
    print("Danh sách tăng dần")
else:
    print("Danh sách không tăng dần")
