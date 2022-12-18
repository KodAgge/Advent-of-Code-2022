import numpy as np
import pandas as pd
from common import load_file

def find_adjacent_sides(coordinates):
    # Finds the number of unique pairs of points that have a touching side
    # If you multiply this number by two, you get the number of non-exposed sides

    df = pd.DataFrame(coordinates, columns=["x", "y", "z"])

    adjacent_sides = 0
    sort_combinations = [["x", "y", "z"], ["y", "z", "x"], ["z", "x", "y"]]

    seen_cube_combinations = set()

    for sort_combination in sort_combinations:
        sorted_df = df.sort_values(list(sort_combination)).to_numpy()
        sorted_df_diff = sorted_df[1:,:] - sorted_df[:-1,:]
        for i, row in enumerate(sorted_df_diff):
            if np.sum(row == 1) == 1 and np.sum(row == 0) == 2:
                cube_combo = tuple(sorted([tuple(sorted_df[i+1]), tuple(sorted_df[i,:])]))
                if cube_combo in seen_cube_combinations:
                    continue
                adjacent_sides += 2
                seen_cube_combinations.add(cube_combo)
    
    return adjacent_sides


def find_possibly_locked_coordinates(coordinates):
    # Finds all coordinates that could be locked inside the droplet
    # We do this by looking at one axis at the time
    # If the point is at least lock in one axis, add it to possibly locked points

    df = pd.DataFrame(coordinates, columns=["x", "y", "z"])

    unique_x = sorted(df["x"].unique())
    unique_y = sorted(df["y"].unique())
    unique_z = sorted(df["z"].unique())

    possibly_locked_coordinates = set()

    for x in unique_x:
        for y in unique_y:
            points = sorted(df[(df["x"] == x)&(df["y"] == y)]["z"].to_numpy())
            if len(points) < 2:
                continue
            for i in range(len(points)-1):
                if points[i+1] - points[i] - 1 == 0:
                    continue
                for z in range(points[i] + 1, points[i+1]):
                    possibly_locked_coordinates.add((x,y,z))

    for y in unique_y:
        for z in unique_z:
            points = sorted(df[(df["y"] == y)&(df["z"] == z)]["x"].to_numpy())
            if len(points) < 2:
                continue
            for i in range(len(points)-1):
                if points[i+1] - points[i] - 1 == 0:
                    continue
                for x in range(points[i] + 1, points[i+1]):
                    possibly_locked_coordinates.add((x,y,z))

    for z in unique_z:
        for x in unique_x:
            points = sorted(df[(df["z"] == z)&(df["x"] == x)]["y"].to_numpy())
            if len(points) < 2:
                continue
            for i in range(len(points)-1):
                if points[i+1] - points[i] - 1 == 0:
                    continue
                for y in range(points[i] + 1, points[i+1]):
                    possibly_locked_coordinates.add((x,y,z))

    cubes = set(map(tuple, coordinates))
    possibly_locked_coordinates -= cubes

    return possibly_locked_coordinates, cubes


def get_moves(coordinate):
    # Returns all positions we have to look at based on a coordinate
    x, y, z = coordinate
    return [(x + dx, y + dy, z + dz) for dx, dy, dz in [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]]


def filter_possibly_locked_coordinates(possibly_locked_coordinates, cubes):
    # Looks at every point in the list of possibly locked points
    # If they only have other possibly locked points or cubes connected to it, it must be locked
    # If at least one point of the pocket is connected to a not possibly locked point
    # the whole pocket isn't locked
     
    not_locked_coordinates = set()
    queue = list(possibly_locked_coordinates)

    while queue:
        coordinate = queue.pop(0)
        sub_queue = [coordinate]
        air_pocket = set(sub_queue)
        locked = True
        while sub_queue:
            next_coordinate = sub_queue.pop(0)
            for next_coordinate in get_moves(coordinate):
                if next_coordinate in not_locked_coordinates:
                    continue
                if next_coordinate in air_pocket:
                    continue
                if next_coordinate in cubes:
                    continue
                if next_coordinate in possibly_locked_coordinates:
                    air_pocket.add(next_coordinate)
                    sub_queue.append(next_coordinate)
                else:
                    locked = False
        if not locked:
            possibly_locked_coordinates -= air_pocket
            not_locked_coordinates |= air_pocket
        
    trapped_air_cubes = list(possibly_locked_coordinates)
    return trapped_air_cubes


read_lines = load_file(test=False)
coordinates = [list(map(int,line.strip().split(","))) for line in read_lines]

# Part 1
# Find the number of sides that are hidden, and subtract them from the maximum number of sides
# that can be visible.

open_sides = 6 * len(coordinates) - find_adjacent_sides(coordinates)
print(f"Answer part 1: {open_sides}")

# Part 2
# Find the number of positions that are locked inside the droplet.
# Then find the number of the number of sides that are adjacent of those points.
# Then the number of open sides inside the droplet is the maximum number of open sides
# of the locked positions minus the number of the common sides of the positions that are locked.
# Then the total number of sides open to outside air is the answer of part 1 minus
# the number of open sides inside the droplet.

possibly_locked_coordinates, cubes = find_possibly_locked_coordinates(coordinates)
trapped_air_cubes = filter_possibly_locked_coordinates(possibly_locked_coordinates, cubes)

trapped_sides = 6 * len(trapped_air_cubes) - find_adjacent_sides(trapped_air_cubes)
print(f"Answer part 2: {open_sides - trapped_sides}")