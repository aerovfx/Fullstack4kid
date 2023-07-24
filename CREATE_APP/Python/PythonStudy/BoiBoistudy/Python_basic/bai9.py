#Nhập số n
n = int(input("Nhập số cần tính giai thừa: "))  
#Hàm tính giai thừa
def giai_thua(n):
    if n==0:   #Nếu i = 0 thì
        return 1   #In 1
    return n*giai_thua(n-1)  #công thức tính giai thừa
#In ra kết quả
print (giai_thua(n))