from collections import deque

def parse_file():
    height_map = [list(map(ord,list(x))) for x in open(file_name).read().strip().splitlines()]
    for r, row in enumerate(height_map):
        for c, height in enumerate(row):
            if height == ord("S"):
                start_row = r
                start_column = c
                height_map[r][c] = ord("a")
            if height == ord("E"):
                end_row = r
                end_column = c
                height_map[r][c] = ord("z")

    height_map = [[height - ord("a") for height in row] for row in height_map]
    
    return (start_row, start_column), (end_row, end_column), height_map

def get_possible_coordinates(row, column, height_map, visited, part):
    possible_coordinates = []
    for new_row, new_column in [(row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1)]:
        if new_row >= MIN_ROW and new_column >= MIN_COLUMN and new_row < MAX_ROW and new_column < MAX_COLUM:
            if (new_row, new_column) not in visited:
                if part == 1:
                    if height_map[new_row][new_column] - height_map[row][column] <= 1:
                        possible_coordinates.append((new_row, new_column))
                elif part == 2:
                    if height_map[new_row][new_column] - height_map[row][column] >= -1:
                        possible_coordinates.append((new_row, new_column))
    return possible_coordinates

def find_route(height_map, part = 1, start = (0, 0), end = (0, 0)):
    (start_row, start_column) = start
    (end_row, end_column) = end

    queue = deque()
    queue.append((0, start_row, start_column))

    visited = {(start_row, start_column)}

    while queue:
        steps, row, column = queue.popleft()
        for new_row, new_column in get_possible_coordinates(row, column, height_map, visited, part):
            if part == 1:
                if new_row == end_row and new_column == end_column:
                    return steps + 1
            elif part == 2:
                if height_map[new_row][new_column] == 0:
                    return steps + 1
            visited.add((new_row, new_column))
            queue.append((steps + 1, new_row, new_column))

file_name = "inputs/12.in"
start, end, height_map = parse_file()
MIN_ROW, MAX_ROW, MIN_COLUMN, MAX_COLUM = 0, len(height_map), 0,  len(height_map[0])

print(f"Answer part 1: {find_route(height_map, part=1, start=start, end=end)}")
print(f"Answer part 2: {find_route(height_map, part=2, start=end)}")