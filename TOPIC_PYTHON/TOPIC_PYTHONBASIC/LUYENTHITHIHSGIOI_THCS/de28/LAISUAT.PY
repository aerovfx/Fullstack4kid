def laisuat(c,t,a,k,h):
    if c!= 0 :
        amount = a*(1+k/100)**c * (1+h/100)**(t-c)
    else:
        amount = a*(1+h/100)*t
    return round(amount, 1)

# doc du lieu
with open('LAISUAT.INP', 'r') as file:
    lines = file.readlines()
    
# in ket qua
result = []
with open('LAISUAT.OUT', 'w') as file:
    for line in lines:
        data = line.split()
        c = int(data[0])
        t = int(data[1])
        a = int(data[2])
        k = float(data[3])
        h = float(data[4])
        
        result = laisuat(c,t,a,k,h)
        file.write(str(result))