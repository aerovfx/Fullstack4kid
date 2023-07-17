def phantulonthu2(numbers):
    if len(numbers)<2:
        print('danh sách này ko đủ phần tử cần thiết')
        return
    
    max1 = max(numbers)
    max2 = None
    vitri_max2 = -1
    
    for i in range(len(numbers)):
        if numbers[i] != max1:
            if max2 is None or numbers[i] > max2:
                max2 = numbers[i]
                vitri_max2 = i
    if max2 is None:
        print('ko tìm thấy phần tử lớn thứ 2')
    else:
        print('phàn tử lớn thứ 2 là: ',max2)
        print('vị trí phần tử lớn thứ 2 là: ', vitri_max2)
numbers = [2,3,4,5,6,7,8,9]
phantulonthu2(numbers)
