from itertools import combinations

def count_combinations(n, k, numbers):
    combinations = set()

    def find_combinations(target, current_combination, visited):
        if target == 0 and len(current_combination) == k:
            sorted_combination = tuple(sorted(current_combination))
            combinations.add(sorted_combination)
            return

        if target < 0 or len(current_combination) > k:
            return

        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                remaining = target - numbers[i]
                find_combinations(remaining, current_combination + [numbers[i]], visited)
                visited[i] = False

    visited = [False] * len(numbers)
    find_combinations(n, [], visited)

    return combinations

with open('DETHI.INP', 'r') as f:
    n, k = map(int, f.readline().split())
    numbers = list(range(1, n + 1))

dethi = count_combinations(n, k, numbers)
count = len(dethi)

with open('DETHI.OUT', 'w') as f:
    f.write(str(count) + '\n')
    for combination in dethi:
        f.write(' '.join(map(str, combination)) + '\n')
