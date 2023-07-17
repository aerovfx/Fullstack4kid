def tinh(numbers):
    min = numbers[0]
    max = numbers[0]
    tong = 0
    for num in numbers:
        if num < min:
            min = num
        if num > max:
            max = num
            
        tong +=num
        
    tb = tong/len(numbers)
    return min,max,tb

# đọc dữ liệu
with open('DAYSO.INP', 'r') as file:
    lines = file.readlines()
    
# in dữ liệu
with open('DAYSO.OUT', 'w') as file:
    for line in lines:
        numbers = [int(num) for num in line.split()]
        
        min, max, tb = tinh(numbers)
        file.write(f'{min} {max} {tb}\n')
