# nhap du lieu
with open('LAISUAT.INP', 'r') as file:
    lines = file.readlines()
    
results = []
for i in range(0, len(lines), 1):
    c,t,a,k,h = map(float, lines[i].split())
    
    if c == 0:
        P = a+a*(h/100)*t
        results.append('{:.1f}'.format(P))
    else:
        P = a*(1+k/100) ** c *(1+h/100)**(t-c)
        results.append('{:.1f}'.format(P))

# in ket qua
with open('LAISUAT.OUT', 'w') as file:
    for result in results:
        file.write(result+'\n')