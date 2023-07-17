def tinh_tbc(a):
    tong = 0
    dem = 0
    ch = 0
    vitri = []
    for i in range(len(a)):
        num = a[i]
        if num > 0:
            tong += num
            dem += 1
        if num%3==0:
            ch += 1
        if num == 0:
            vitri.append(i)
    tbc = tong / dem 
    print("Trung bình cộng các số dương trong dãy: ", tbc)
    print('có:',ch,'số chia hết cho 3')
    print('vị trí các số bằng 0: ',vitri)
danh_sach = [2, 4, -5, 8, 0, 9, 0, 12, -6, 10]
tinh_tbc(danh_sach)
