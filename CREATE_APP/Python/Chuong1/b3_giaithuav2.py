input_file = 'b3_GIAITHUA.INP'
output_file = 'b3_GIAITHUA.OUT'

def fact(n):
    if n == 0 :
        return 1
    else:
        return n*fact(n-1)
    
with open(input_file,'r') as file:
    numbers = file.read().strip().split()
result_string = ''
for num in numbers:
    num = int(num)
    giai_thua_num = fact(num)
    result_string += str(fact(num)) + '\n'
    
with open(output_file,'w') as file:
    file.write(result_string)