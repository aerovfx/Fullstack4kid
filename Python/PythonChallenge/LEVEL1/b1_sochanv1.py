#Bài 1. In toàn bộ các số chẵn từ 1000 đến 2000
even_numbers=[] # gán số chẵn là mãng rỗng
for i in range(1, 10): # lặp i chạy từ 1 đến 10
    if (i%2==0): # nếu i chia hết cho 2 thì
        even_numbers.append(str(i)) # ghi chuỗi vào cuối mãng
print (','.join(even_numbers)) # nối các phần tử của mãng phân cách bởi dấu phẩy