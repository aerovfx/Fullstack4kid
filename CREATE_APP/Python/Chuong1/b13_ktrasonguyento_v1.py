def ngto(n):
    for i in range(2, n):
        if n % i == 0:
            print('day ko phai la so nguyen to', n)
            break
        else:
            print('day la so nguyen to',n) 


n_list = 4 ,8, 5

result_string =""
for num in n_list:
    num = int(num)
    ngto_num = ngto(num)
    result_string +=  str(ngto_num) + "\n"

print(result_string)