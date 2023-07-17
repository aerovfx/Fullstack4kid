# lập hàm đếm số gà và chó
def chan_ga_cho(total_legs):
    solutions = [] # danh sách lưu trữ các giải pháp
    for chan_ga in range(1, total_legs+1): # duyệt số lương gà từ 1 đến 101
        for chan_cho in range(1, total_legs+1):
            if 2 * chan_ga +4 * chan_cho == total_legs: 
                solutions.append((chan_ga, chan_cho))
    return solutions

# đọc tổng số chân gà và chó
with open('TOANCO.INP', 'r') as file:
    total_legs = int(file.readline())
# tìm giải pháp gọi hàm đếm số chân gà và chó 
results = chan_ga_cho(total_legs)

# ghi giải pháp tìm được vào file
with open('TOANCO.OUT', 'w') as file:
    if len(results) >0:
        file.write('kết quả phù hợp: \n')
        for chan_ga, chan_cho in results:
            file.write(f'so ga: {chan_ga} \n ')
            file.write(f'so cho: {chan_cho} \n')
            
    else:
        file.write('ko tìm được số chân gà và chó \n')