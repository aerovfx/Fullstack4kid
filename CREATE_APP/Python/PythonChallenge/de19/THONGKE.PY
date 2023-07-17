def dem_tuansuat(n):
    tuansuat = {}
    for num in n:
        if num in tuansuat:
            tuansuat[num] += 1
        else:
            tuansuat[num] = 1
    return tuansuat 

with open('THONGKE.INP', 'r') as file:
    chuoi_so = file.readlines()
    numbers_list = [chuoi.strip().split() for chuoi in chuoi_so]
result = []
for num in chuoi_so:
    num = int(num)
    kq = dem_tuansuat(num)
    result = kq
with open('THONGKE.OUT', 'w') as file:
    for freq in chuoi_so:
            for num, count in freq.items():
                file.write(f"{num}({count}) ")
            file.write("\n")

