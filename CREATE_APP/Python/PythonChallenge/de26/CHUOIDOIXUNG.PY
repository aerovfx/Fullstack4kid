def chuoidoixung(chuoi): # hàm kiểm tra có là chuỗi đối xứng ko
    chuoidaonguoc = chuoi[::-1] # chuỗi đảo ngược
    if chuoi == chuoidaonguoc:
        return True
    else:
        return False
    
input = input('nhap 1 chuoi: ') # nhập chuõi từ bàn phím
if chuoidoixung(input): # kiểm tra chuỗi rồi in ra kết quả
    print('day la chuoi doi xung')
else:
    print('day ko la chuoi doi xung')
