def count_rotation(directions, target_direction):
    rotation_count = 0
    for direction in directions:
        if direction == target_direction:
            rotation_count += 0
        elif direction == 1 and target_direction == 2:
            rotation_count += 2
        elif direction == 2 and target_direction == 1:
            rotation_count += 2
        elif abs(direction - target_direction) == 1:
            rotation_count += 1
        elif abs(direction - target_direction) == 3:
            rotation_count += 1
        else:
            rotation_count += 2
    return rotation_count

def find_best_direction(directions):
    min_rotation = float('inf')
    best_direction = None

    for target_direction in range(1, 5):
        rotation_count = count_rotation(directions, target_direction)
        if rotation_count < min_rotation:
            min_rotation = rotation_count
            best_direction = target_direction

    return best_direction, min_rotation

def main():
    with open('DOIHUONG.INP', 'r') as f_in:
        test_cases = f_in.read().splitlines()

    with open('DOIHUONG.OUT', 'w') as f_out:
        for test_case in test_cases:
            directions = list(map(int, test_case.strip()))
            best_direction, min_rotation = find_best_direction(directions)
            f_out.write(f"{best_direction}\n{min_rotation}\n")

if __name__ == "__main__":
    main()
