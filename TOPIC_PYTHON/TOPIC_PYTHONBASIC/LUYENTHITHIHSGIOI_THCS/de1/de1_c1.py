def S_hv(a, b,c ):
    if (a*a == b*b + c*c): return (1/2)*b*c
    if (b*b == a*a + c*c): return (1/2)*a*c
    if (c*c == b*b + a*a): return (1/2)*b*a

    return -1 #Khong phai la tam giac vuong

f_in = open("TAMGIAC.INP","r"); f_out = open("TAMGIAC.OUT","w") #Mở 2 file
line = f_in.readline().split() # chuyển chuỗi thành mảng 1 chiều
int_a = [int(x) for x in line] #tạo mảng số nguyên từ mảng trên (ép kiểu dữ liệu)
dientichhinhvuong = S_hv(int_a[0], int_a[1], int_a[2]) #gọi hãm diện tích hình vuông với các tham số là các phần tử của mảng số nguyên
f_out.write(str(round(dientichhinhvuong,1))) #ghi vào file TAMGIAC.OUT kết quả và làm tròn 1 đơn vị.
f_in.close(); f_out.close(); #Đóng 2 file trên.
