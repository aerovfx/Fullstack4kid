def thongson():
    n = int(input('nhập số n: '))
    if n <=0 or n > 50:
        print('thông số n ko hợp lệ')
        return
    
    danh_sach = []
    for i in range(n):
        chiso = float(input('nhập vào chỉ số thứ {i+1}:'))
        danh_sach.append(chiso)
        
    # tìm tổng số nguyên dương chẵn:
    count = 0
    for chiso in danh_sach:
        if chiso % 2 == 0 and chiso>0:
            count += 1
            
    # tìm số âm lớn nhất:
    max_am = None
    chisoamln = []
    for i in range(len(danh_sach)):
        if max_am is None or danh_sach[i] > max_am:
            max_am = danh_sach[i]
            chisoamln = [i]
        elif danh_sach[i] == max_am:
            chisoamln.append(i)
            
    # Tìm tất cả các dãy con dài nhất các số dương cùng dấu
    danh_sach_con = []
    con = []
    for chiso in danh_sach:
        if not con or (con[-1] > 0 and chiso > 0) or (con[-1] < 0 and chiso< 0):
            con.append(chiso)
        else:
            if con[-1] > 0:
                danh_sach_con.append(con)
            con = [chiso]
    if con and con[-1] > 0:
        danh_sach_con.append(con)
        
        
    #in kết quả
    print('tổng số nguyên dương chẵn là: ',count)
    print('số âm lớn nhất là: ',chisoamln)
    print('tất cả các dãy con dài nhất các số dương cùng dấu là: ')
    for j in danh_sach_con :
        print(j)
        
if __name__ == '__thongson__':
    thongson()

