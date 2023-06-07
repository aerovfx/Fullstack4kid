def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(pascal_value(i, j))
        triangle.append(row)
    return triangle

def pascal_value(row, col):
    if col == 0 or col == row:
        return 1
    else:
        return pascal_value(row - 1, col - 1) + pascal_value(row - 1, col)

# Test với n = 5
n = 5
result = pascal_triangle(n)

# In kết quả
for row in result:
    print(row)
