def tim_chuoi_con(sequence): #ham tim chuoi con lien tiep squence nghia la lien tiep
    n = len(sequence)
    chuoi = []
    for i in range(n):
        for j in range(i+1, n+1):
            chuoi.append(sequence[i:j])
    return chuoi

with open('CHUOICON.INP', 'r') as file:
    sequence = file.read().strip().split(',')
    
# chuyển các phần tử trong chuỗi thành số nguyên # dùng này rồi thì duối đóng vô#
#sequence = [int(num) for num in sequence] # sử dunnjg 1 trong 2 cái này
# loại bỏ dấu ngoặc "[" và "]" dùng này thì đóng ở trên như đang đóng#
sequence = [num.strip('[').strip(']') for num in sequence]


chuoi = tim_chuoi_con(sequence)
    
with open('CHUOICON.OUT', 'w') as file:
    for chuoicon in chuoi:
        file.write(','.join(map(str, chuoicon)) + '\n')
    