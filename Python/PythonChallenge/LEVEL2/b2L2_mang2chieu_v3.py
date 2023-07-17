#tao ham
def mang2_chieu(rowNum, colNum):
    multilist = [[row * col for col in range(colNum)] for row in range(rowNum)]
    return multilist

#mở file input và đọc từng dòng lệnh, với x,y thì gọi hàm create_multilist và ghi vào biến tên là results
with open('b2L2_MANG2CHIEU.INP', 'r') as file:
    lines = file.readlines()
    
results = []
for line in lines:
    dimension = [int(x) for x in line.strip().split(',')]
    rowNum, colNum = dimension
    result = mang2_chieu(rowNum, colNum)
    results.append(str(result))
    
with open('b2L2_MANG2CHIEU.OUT', 'w') as file:
    for result in results:
        for row in result:
            file.write(','.join(results)+ '\n')
            file.write('\n')