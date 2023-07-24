#Nhập số n
n = int(input("Nhập số cần tính giai thừa: "))  
#Hàm tính giai thừa
def giai_thua(n):
    if n == 0:
        return 1
    return n *giai_thua(n - 1)
#In ra kết quả
print (giai_thua(n))