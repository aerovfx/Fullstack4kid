input_file = "b1_SOCHAN.INP"
output_file = "b1_SOCHAN.OUT"

with open(input_file, 'r') as file:
    numbers = file.read().strip().split()

so_chan = []
so_le = []

for i in numbers:
    i = int(i)
    if i %2 == 0 :
        so_chan.append(str(i))
    else:
        so_le.append(str(i))
        
result_string = "so chan la: " + ",".join(so_chan) + "\n"
result_string += "so le la: " + ",".join(so_le)

with open(output_file, 'w') as file:
    file.write(result_string)