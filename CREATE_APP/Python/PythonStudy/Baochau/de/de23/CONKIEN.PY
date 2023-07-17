def find_min_time(n, m, l, kiens):
    group = []
    groups = []
    tong_m = 0
    
    for i in range(n):
        weight, speed = kiens[i]
        
        if tong_m + weight>m:
            groups.append(group)
            group = []
            tong_m = 0
        group.append(kiens[i])
        tong_m += m
    if group:
        groups.append(group)
    min_time = 0
    for group in groups:
        min_speed = min(group, key = lambda x: x[1])[1]
        time = l/min_speed
        min_time += time
    return min_time

with open('CONKIEN.INP', 'r') as file:
    n, m, l = list(map(int, file.readline().split()))
    kiens = [list(map(int, line.split(' '))) for line in file]
    
tong_tgian = find_min_time(n, m, l , kiens)
with open('CONKIEN.OUT', 'w') as file:
    file.write(str(tong_tgian))