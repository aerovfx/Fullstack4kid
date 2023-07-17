#Đây là một phiên bản chương trình tương tự, nhưng thay vì tìm các số trong đoạn từ 2000 đến 3200, 
#chương trình này sẽ yêu cầu người dùng nhập một chuỗi số và kiểm tra xem các số trong chuỗi có chia hết cho 7 
#và không phải là bội số của 5 hay không.
so = input('nhap vao cac so, cac so cach nhau dau phay: ')
so = so.split(',')

ket_qua = []
for i in so:
    i = int(i)
    if i%7==0 and i%5!=0:
        ket_qua.append(str(i))
ket_qua = 'cac so chia het cho 7 nhung khong la boi cua 5 la: ' + ','.join(ket_qua)
print(ket_qua)