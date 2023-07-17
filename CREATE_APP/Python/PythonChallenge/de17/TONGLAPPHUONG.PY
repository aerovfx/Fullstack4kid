def soc(n):
    cac_so = list(map(int, n.split()))
    tong = sum([x**3 for x in cac_so])
    return tong

with open("TONGLAPPHUONG.INP", "r") as file:
    numbers = file.readlines()
   
results = [] 
for num in numbers:
    lap_phuong = soc(num)
    results.append(lap_phuong)
    
with open('TONGLAPPHUONG.OUT', 'w') as file:
    for result in results:
        file.write(str(result) + '\n')