from array import *

file =  open("ORDER.INP")
file2 = open("ORDER.OUT", "w")

n = int(file.readline())
a = array('i')
dem = array('i')

for i in range(n):
    temp = int(file.readline())
    a.append(temp)
    
m = max(a)
for i in range(m+1):
    dem.append(0) #gán số lượng bán ban đầu là 0
    
for i in range(n):
    j = a[i]
    dem[j] += 1 # tăng giá trị bién đếm lên 1

kq = max(dem)
file2.write(str(kq))

file.close()
file2.close()