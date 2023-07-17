def so_hanhphuc(n): # hàm kiểm tra số hạnh phúc
    xem = set() # lưu trữ những số đã xem
    
    while n != 1 and n not in xem:
        xem.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

# đọc dữ liệu
with open('SOHANHPHUC.INP', 'r') as file:
    numbers = file.readline()
    
# in dữ liệu
with open('SOHANHPHUC.OUT', 'w') as file:
    for number in numbers:
        numbers = int(number.strip())
        if so_hanhphuc(number):
            file.write(str(number) + 'la so hanh phuc '+'\n')
        else:
            file.write(str(number) + 'ko la so hanh phuc'+'\n')