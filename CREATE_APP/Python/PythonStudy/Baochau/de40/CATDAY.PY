with open('CATDAY.INP', 'r') as file:
    n = int(file.read())    
count = 0
for x in range(1, n):
    y = n-2 * x
    if x + x > y and y > x:
        count += 1
        print(x,y)
        

with open('CATDAY.OUT', 'w') as file:
    file.write(str(count))