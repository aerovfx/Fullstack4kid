# To calculate the number of tiles needed, you can add the number of tiles needed for each part of the floor:
part1_width = 9
part1_length = 7

part2_width = 5
part2_length = 7

total_tiles_needed = (part1_width * part1_length) + (part2_width * part2_length)
print("Number of tiles needed:", total_tiles_needed)

# To calculate the number of tiles left over after buying 17 packages of tiles,
# you can subtract the total number of tiles needed from the number of tiles in the packages:
packages = 17
tiles_per_package = 6

total_tiles = packages * tiles_per_package
tiles_left_over = total_tiles - total_tiles_needed
print("Number of tiles left over:", tiles_left_over)
