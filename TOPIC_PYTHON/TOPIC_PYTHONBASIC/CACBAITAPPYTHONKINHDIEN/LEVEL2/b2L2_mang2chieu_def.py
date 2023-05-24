def create_multilist(rowNum, colNum):
    multilist = [[row * col for col in range(colNum)] for row in range(rowNum)]
    return multilist

input_str = input("Nhập X, Y: ")
dimensions = [int(x) for x in input_str.split(',')]
rowNum, colNum = dimensions

result = create_multilist(rowNum, colNum)
print(result)
