import math

# đọc dữ liệu
with open('ROOT.INP', 'r') as file:
    lines = file.readlines()
    a = int(lines[0])
    b = int(lines[1])
    c = int(lines[2])
    
# tính giá trị
s = (a**2 + b**2 + c**2)/(a*b*c) + math.sqrt(a*b*c)

# ghi kết qủa vào file:
with open('ROOT.OUT', 'w') as file:
    file.write('{:.2f}'.format(s))