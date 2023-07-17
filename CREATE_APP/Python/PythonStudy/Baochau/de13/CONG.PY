#ham tinh cong
def cong(p,t):
    cong = int(p)*int(t)
    return cong


# doc du lieu tu ngoai
with open('CONG.INP', 'r') as file:
    lines = file.readlines()
    
results = []
for line in lines:
    cong_list = line.strip().split(' ')
    p,t = map(int, cong_list) # chuyển đổi thành danh sách số nguyên
    
    result = cong(p,t)
    results.append(result)
    
# in ket qua
with open('CONG.OUT', 'w') as file:
    file.write(f'{results}\n')