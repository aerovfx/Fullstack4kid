def tsln_nn(number):
    min= number[0]  # Giả sử phần tử đầu tiên là phần tử nhỏ nhất
    min2 = float('inf')  # khởi tạo giá trị ban đầu của biến second_min_num là một số dương vô cùng.
    max = number[0]  # Giả sử phần tử đầu tiên là phần tử lớn nhất
    vitri_max = 0
    
    for i in range(len(number)):
        num = number[i]
        if min>num:
            min2 = min
            min = num
        if min2 > num and num != min:
            min2 = num
        if max < num:
            max = num
            vitri_max = i
    return min,min2,vitri_max


number = [-4, 5, -0, 90, -7]
min, min2, vitri_max = tsln_nn(number)
print('phan tu nho nhat: ',min)
print('phan tu nho thu 2: ',min2)
print('Vi tri phan tu lon nhat: ',vitri_max)
