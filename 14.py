from common import load_file
import numpy as np

def create_map_array(read_lines):
    paths = [[list(map(int,coordinate.split(","))) for coordinate in path.strip().split(" -> ")] for path in read_lines]
    all_coordinates = []
    for path in paths:
        for coordinate in path:
            all_coordinates.append(coordinate)

    all_coordinates = np.array(all_coordinates)

    MIN_X = np.min(all_coordinates[:,0])
    MAX_X = np.max(all_coordinates[:,0])

    MIN_Y = np.min(all_coordinates[:,1])
    MAX_Y = np.max(all_coordinates[:,1])

    map_array = np.zeros((MAX_Y+1, MAX_X-MIN_X+1))

    for path in paths:
        for i in range(len(path)-1):
            x1, y1 = path[i]
            x2, y2 = path[i+1]
            if y1 == y2:
                for x in range(min(x1, x2), max(x1, x2)+1):
                    map_array[y1,x-MIN_X] = 1
            elif x1 == x2:
                for y in range(min(y1, y2), max(y1, y2)+1):
                    map_array[y,x1-MIN_X] = 1
    
    return map_array, MIN_X, MAX_X, MIN_Y, MAX_Y

def print_readable(map_array):
    string = ""
    for row in map_array.tolist():
        for value in row:
            string += "." if value == 0 else ("#" if value == 1 else "o")
        string += "\n"
    print(string)


def simulate_sand(map_array):
    out_of_bounds = False
    sand_count = 0
    while not out_of_bounds:
        sand_x, sand_y = DROP_COORDINATES
        sand_in_rest = False
        while not sand_in_rest:
            if sand_x < MIN_X or sand_x >= MAX_X or sand_y >= MAX_Y:
                out_of_bounds = True
                break
            if map_array[sand_y+1,sand_x-MIN_X] == 0:
                sand_y += 1
            elif map_array[sand_y+1,sand_x-MIN_X-1] == 0:
                sand_y += 1
                sand_x -= 1
            elif map_array[sand_y+1,sand_x-MIN_X+1] == 0:
                sand_y += 1
                sand_x += 1
            else:
                sand_count += 1
                sand_in_rest = True
                map_array[sand_y, sand_x-MIN_X] = 2
                if sand_y == DROP_COORDINATES[1]:
                    out_of_bounds = True
                    break

    # print_readable(map_array)
    return sand_count

read_lines = load_file()
DROP_COORDINATES = [500, 0]

# Part 1
map_array, MIN_X, MAX_X, MIN_Y, MAX_Y = create_map_array(read_lines)
print(f"Answer part 1: {simulate_sand(map_array)}")

# Part 2
read_lines.append(f"{MIN_X-200},{MAX_Y+2} -> {MAX_X+200},{MAX_Y+2}")
map_array, MIN_X, MAX_X, MIN_Y, MAX_Y = create_map_array(read_lines)
print(f"Answer part 2: {simulate_sand(map_array)}")