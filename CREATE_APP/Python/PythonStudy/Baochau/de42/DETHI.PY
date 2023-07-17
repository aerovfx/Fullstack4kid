from itertools import combinations

def dem_combinations(n, k, numbers):
    combinations = set()
    
    def tim_combinations(target, hientai_combinations, visited):
        if target == 0 and len(hientai_combinations) == k:
            sapxep_combination = tuple(sorted(hientai_combinations))
            combinations.add(sapxep_combination)
            return
        
        if target < 0 or len(hientai_combinations) > k:
            return
        
        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                remaining = target - numbers[i]
                tim_combinations(remaining, hientai_combinations + [numbers[i]], visited)
                
    visited = [False] * len(numbers)
    tim_combinations(n, [], visited)
    
    return combinations

with open('DETHI.INP', 'r') as file:
    n, k = map(int, file.readline().split())
    numbers = list(range(1, n+1))

dethi = dem_combinations(n, k, numbers)
dem = len(dethi)

with open('DETHI.OUT', 'w') as file:
    file.write(str(dem) + '\n')
    for combination in dethi:
        file.write(' '.join(map(str, combination)) + '\n')