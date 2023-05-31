def can_pass(time, ants, m):
    group_weight = 0
    group_time = 0
    for ant in ants:
        group_weight += ant[0]
        if group_weight > m:
            return False
        group_time = max(group_time, ant[0] / ant[1])
        if group_time > time:
            return False
    return True

def binary_search(ants, m):
    low = 0
    high = sum(ant[0] for ant in ants) / min(ant[1] for ant in ants)
    while low < high:
        mid = (low + high) / 2
        if can_pass(mid, ants, m):
            high = mid
        else:
            low = mid + 1
    return low

def main():
    with open('CROUANTS.INP', 'r') as f:
        n, m, l = map(int, f.readline().split())
        ants = []
        for _ in range(n):
            k, v = map(int, f.readline().split())
            ants.append((k, v))
    
    ants.sort() # Sắp xếp các con kiến theo thứ tự tăng dần của khối lượng
    
    min_time = binary_search(ants, m) # Tìm thời gian nhỏ nhất
    
    with open('CROUANTS.OUT', 'w') as f:
        f.write("{:.2f}".format(min_time))
    
if __name__ == '__main__':
    main()
