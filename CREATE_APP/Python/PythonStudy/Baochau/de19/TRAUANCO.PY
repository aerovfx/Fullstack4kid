def so_trau():
    for i in range(1,101):
        for j in range(1,101):
            k = 100 - i - j
            if 14*i + 8*j == 200 and k >= 0:
                return (i,j,k)
    return None       

result = so_trau()
if result :
    print('số trâu đứng, số trâu nằm, số trâu già theo thứ tự là:', result)
else:
    print('ko tìm thấy kết quả')

