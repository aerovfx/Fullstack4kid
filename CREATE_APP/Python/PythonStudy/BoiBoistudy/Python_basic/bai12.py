import math
def can_bac_hai(danh_sach):
    a = math.sqrt(danh_sach)
    return a

# Đọc dữ liệu từ file "BAI12":
with open('BAI12.INP', 'r') as file:
    danh_sach = list(map(int, file.readline().split(",")))
for i in range(1, danh_sach):
    
    
#Xuất dữ liệu ra file "BAI12":
with open('BAI12.OUT','w') as file:
    file.write(str(danh_sach))