import math
def ptb2(a,b,c):
    delta = b*b-4*a*c
   
    if delta < 0:
        return None
    if delta == 0:
        x =-b/(2*a)
        return [x]
    if delta > 0:
        x1 = (-b + math.sqrt(delta))/2*a
        x2 = (-b - math.sqrt(delta))/2*a
        return [x1, x2]

# đọc file
with open('PTB2.INP', 'r') as file:
    numbers = file.readlines()
    
# in dữ liệu
with open('PTB2.OUT', 'w') as file:
    for num in numbers:
        a,b,c= map(int, num.strip().split(' '))
        solutions = ptb2(a,b,c)
        if solutions is None:
            file.write('PTVN\n')
        else:
            file.write('x')
            for solution in solutions:
                file.write(str(solution) + '')
            file.write('\n')