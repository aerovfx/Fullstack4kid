#Bài 14. Viết một chương trình nhập vào hai số tự nhiên m, n. In ra màn hình mảng hai chiều mà phần tử trong hàng thứ i và cột thứ j của mảng là i*j.
m, n = int(input)
array2 = [[0 for i in range(n)] for j in range(m)]
for row in range(m):
    for col in range(n):
        array2[row][col] = row * col
print(array2)

with open('b14_INMANG.INP', 'r') as file:
    array = file.read().strip().split()
  
  
result_string =""
for num in array:
    num = int(num)
    mang_num = array(num)
    result_string +=  str(mang_num) + "\n"


# Ghi kết quả vào file b13_NGUYENTO.OUT
with open( 'b14_INMANG.OUT',"w") as file:
    file.write(result_string)  
