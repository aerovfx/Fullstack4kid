# ham ve tam giac pascal
def paint_pascal(n):
    tamgiac = [] # danh sach rong luu tam giac pascal
    for i in range(n):
        row = [] # hang rong
        for j in range(i+1):
            row.append(value_pascal(i,j)) # them gia tri cac phan tu cua tung hang
        tamgiac.append(row) # them hang vao tam giac pascal
    return tamgiac # tra ve tam giac pascal da tao

# ham tinh gia tri cac phan tu trong tam giac
def value_pascal(row,col):
    if col == 0 or row == col:
        return 1 # tra ve gia tri cua phan tu bien va dinh la 1
    else:
        # gia tri cua o bat ki laf tong 2 o phia tren no
        return value_pascal(row-1, col) + value_pascal(row-1, col-1)

# test gia tri voi n = 5 va in ket qua
n = 15
result = paint_pascal(n) # goi ham
for row in result:
    print(row) # in tung hang mot