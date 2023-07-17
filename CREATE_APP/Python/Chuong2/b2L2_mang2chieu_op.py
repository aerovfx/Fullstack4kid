input_str = input("Nhập X, Y: ")
dimensions = [int(x) for x in input_str.split(',')]
rowNum, colNum = dimensions
multilist = [[row * col for col in range(colNum)] for row in range(rowNum)]

print(multilist)