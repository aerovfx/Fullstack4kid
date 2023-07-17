with open('MOD5.INP', 'r') as file:
    numbers = file.read().strip().split()
    
chia_het = []
for num in numbers:
    num = int(num)
    if num % 5 == 0:
        chia_het.append(str(num))
        
result = ' '.join(chia_het)
with open('MOD5.OUT', 'w') as file:
    file.write(result)