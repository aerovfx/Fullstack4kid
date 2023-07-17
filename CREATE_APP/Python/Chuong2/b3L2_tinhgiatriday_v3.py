def calculate_sequence_value(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4
    else:
        a = 2
        b = 4
        for i in range(3, n+1):
            c = b+(i-2)*3
            a = b
            b = c
            return c

input_file = 'b3L2_INGIATRIDAY.INP'
output_file = 'b3L2_INGIATRIDAY.OUT'

# mở và tách chuỗi ( dùng lệnh split)
with open(input_file, 'r') as file:
    lines = file.readlines()
    
# xử lí dữ liệu
results = []
for line in lines:
    values = line.strip().split(',')
    for value in values:
        n = int(n)
        chuoi = calculate_sequence_value(n)
        results.append(chuoi)



with open(output_file, 'w') as file:
    for result in results:
        file.write(f'{result}\n')
