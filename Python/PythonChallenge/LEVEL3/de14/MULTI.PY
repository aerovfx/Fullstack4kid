def multi(x,y):
    mul = int(x)*int(y)
    return mul

# doc du lieu
with open('MULTI.INP', 'r') as file:
    lines = file.readlines()
    
results = []
for line in lines:
    multi_list = line.strip().split(' ')
    x,y = map(int, multi_list)
    
    result = multi(x,y)
    results.append(result)
    
# in du lieu vao file
with open('MULTI.OUT', 'w') as file:
    file.write(f'{results}\n')