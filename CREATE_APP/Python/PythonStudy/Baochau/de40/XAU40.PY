# Đọc xâu đầu vào từ bàn phím. 
string = input('nhập vào chuỗi xâu: ')
#Khởi tạo một danh sách rỗng để lưu trữ các xâu con. 

def tao_chuoicon(string):
    danh_sach = []
    n = len(string)
#Với mỗi vị trí i từ 0 đến chiều dài của xâu đầu vào: 
    for i in range(n):
#Với mỗi vị trí j từ i+1 đến chiều dài của xâu đầu vào: 
        for j in range(i+1, n+1):
#Thêm xâu con từ vị trí i đến vị trí j vào danh sách. 
            danh_sach.append(string[i:j])
#In tất cả các xâu con trong danh sách.
    return danh_sach
results = tao_chuoicon(string)
for result in results:
    print(result)