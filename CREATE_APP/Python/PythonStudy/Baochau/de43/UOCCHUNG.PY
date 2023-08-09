def tim_phan_tu(n):
    if n==1 :
        gia_tri = 1 
    if n>1:
        num = n-1 
        gia_tri = num + num 
    return gia_tri
with open('Cstn.INP','r') as file:
    kq = tim_phan_tu(n)
with open('Cstn.OUT','w') as file:
    file.write('\n') 