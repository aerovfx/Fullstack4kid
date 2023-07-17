def hieusuat(P,t,m,h):
    cci = int(m)*1000*10*int(h)
    ctp = int(P)*int(t)* 3600
    efficiency = (cci/ctp) *100
    return efficiency

# dữ liệu vào
with open('TUVAN.INP', 'r') as file:
    numbers = file.readlines()
    
results = []
for num in numbers:
    hs_list = num.strip().split(' ')
    cong_suat = int(hs_list[0])
    thoi_gian = int(hs_list[1])
    m_nuoc = int(hs_list[2])
    do_cao = int(hs_list[3])
    
    hieu_suat = hieusuat(cong_suat, thoi_gian, m_nuoc, do_cao)
    results.append(hieu_suat)
    
with open('TUVAN.OUT', 'w') as file:
    file.write(f'{results}%\n')