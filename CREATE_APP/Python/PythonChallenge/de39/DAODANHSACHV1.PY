def daolist(danhsach):
    return danhsach[::-1]

# nhap vao danh sach
danhsach = input('nhap vao 1 chuoi: ')
# xoá các khoảng trống ở đầu và cuối các phàn tử
danhsach = [item.strip() for item in danhsach]

# đảo ngược danh sách
daodanhsach = daolist(danhsach)
print('danh sách sau khi đảo ngược là: ', daodanhsach)

