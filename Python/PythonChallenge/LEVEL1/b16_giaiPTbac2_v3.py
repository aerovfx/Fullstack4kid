def pt2(a,b,c):
    if a == 0:
        if b == 0:
            if c == 0:
                return("Phương trình có vô số nghiệm")
            else:
                return("Phương trình vô nghiệm")
        else:
            return -c/b
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            return("Phương trình vô nghiệm")
        elif delta == 0:
            return -b/(2*a)
        else:
            return (-b - delta**0.5)/(2*a)
        
with open('b16_PTBAC2.INP', 'r') as file:
    pt = file.read().strip().split(',')

# ktra và chuyển đổi thành số nguyên

a,b,c = map(int, pt) # map chuyển danh sách thành số nguyên
    

with open('b16_PTBAC2.OUT', 'w') as file:
    result_string = str(pt2(a,b,c))
    file.write(''.join(result_string))
