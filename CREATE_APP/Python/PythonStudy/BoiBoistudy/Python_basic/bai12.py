import math
# Đọc dữ liệu từ file "BAI12":
def can_bac_hai(danh_sach):
    a = math.sqrt(danh_sach)
    return a

n=int(input('Nhập vào 1 số:'))
print(can_bac_hai(n))