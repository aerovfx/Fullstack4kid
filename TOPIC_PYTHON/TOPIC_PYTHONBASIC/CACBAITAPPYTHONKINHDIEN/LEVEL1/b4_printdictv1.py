#Bài 4. Với số nguyên n nhất định, hãy viết chương trình để tạo ra một dictionary chứa (i, i*i) 
#như là số nguyên từ 1 đến n (bao gồm cả 1 và n) sau đó in ra dictionary này. 
#Ví dụ: Giả sử số n là 8 thì đầu ra sẽ là: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}.
n = int(input('Enter a number ')) #nhap va mot so nguyen
d = dict() #gan bien d la mot tu dien rong.
for i in range(1, n+1): #lap i tu 1 den n+1
    d[i] = i*i #phan tu thu i cua tu dien gan ban i*i
print(d) #in ra gia tri cua dict d.