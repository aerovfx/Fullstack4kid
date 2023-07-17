with open('SO_CHAN.INP', 'r') as file:
    numbers = file.read().strip().split()
    
so_chan = []


for i in numbers:
    i = int(i)
    if i % 2 == 0:
        so_chan.append(str(i))
    
  
result_str = 'so chan la: '+ ','.join(so_chan)      
with open('SO_CHAN.OUT', 'w') as file:
    file.write(result_str )