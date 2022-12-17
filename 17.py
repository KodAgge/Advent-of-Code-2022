
import numpy as np
from common import load_file

def print_chamber(chamber):
    string = ""
    for row in chamber[max_y-4:,:width]:
        for value in row:
            string += "o" if value == 0.5 else ("@" if value == 2 else ("#" if value == 1 else "."))
        string += "\n"
    print(string)

def print_chamber_falling_rock(chamber, rock, x, y):   
    chamber_and_rock = chamber.copy()
    chamber_and_rock[y-4:y, x:x+4] += 2 * rock
    string = ""
    for row in chamber_and_rock[max_y-4:,:width]:
        for value in row:
            string += "o" if value == 0.5 else ("@" if value == 2 else ("#" if value == 1 else "."))
        string += "\n"
    print(string)

def get_rocks():
    shapes = []

    shape_1 = np.zeros((4,4))
    shape_1[3,:] = 1
    shapes.append(shape_1)

    shape_2 = np.zeros((4,4))
    shape_2[2,0:3] = 1
    shape_2[1:4,1] = 1
    shapes.append(shape_2)

    shape_3 = np.zeros((4,4))
    shape_3[3,0:3] = 1
    shape_3[1:4,2] = 1
    shapes.append(shape_3)

    shape_4 = np.zeros((4,4))
    shape_4[:,0] = 1
    shapes.append(shape_4)

    shape_5 = np.zeros((4,4))
    shape_5[2:4,0] = 1
    shape_5[2:4,1] = 1
    shapes.append(shape_5)

    return shapes

def initiate_chamber(n_rocks, start_pos):
    height = (n_rocks + 1) * 4 
    padding = 3
    width = 7 + 2
    chamber = np.zeros((height, width+padding))
    chamber[:, 0] = 0.5
    chamber[:, width - 1] = 0.5

    start_pos_height = start_pos.shape[0]
    chamber[-1-(start_pos_height-1):, 1:8] = start_pos

    return chamber, height, width, padding

def simulate_rock_falling(chamber, rock, winds):
    max_y = np.where(np.sum(chamber[:,1:-4] > 0, axis=1))[0][0] - 3
    x = 3
    y = max_y
    at_rest = False
    while not at_rest:
        # Wind
        wind = winds.pop(0)
        winds.append(wind)
        if wind == ">":
            if np.sum(chamber[y-4:y, x+1:x+5]+rock > 1) == 0:
                x += 1
        else:
            if np.sum(chamber[y-4:y, x-1:x+3]+rock > 1) == 0:
                x -= 1
        # Move
        if np.sum(chamber[y-3:y+1, x:x+4]+rock > 1) == 0:
            y += 1
        else:
            at_rest = True
        if at_rest:
            chamber[y-4:y, x:x+4] += rock
            break
    return chamber, winds

# Part 1
print("Part 1 version 1:")
rocks = get_rocks()
winds = [*load_file()[0]]
n_rocks = 2022
height = (n_rocks + 1) * 4 
start_pos = np.ones((1,7))

chamber, height, width, padding = initiate_chamber(n_rocks, start_pos)
max_y = 0

for i in range(n_rocks):
    rock = rocks.pop(0)
    rocks.append(rock)
    max_y = np.where(np.sum(chamber[:,1:-4] > 0, axis=1))[0][0] - 3
    x = 3
    y = max_y
    at_rest = False

    chamber, winds = simulate_rock_falling(chamber, rock, winds)

max_height = height - np.where(np.sum(chamber[:,1:-4] > 0, axis=1))[0][0] - 1
print(f"\tAnswer: {max_height}")

# ===== HEAVILY OPTIMIZED VERION =====
# What we now do is to look after a combination of wind, rock and rock pile we will see twice.
# If we see it twice, it means that we can jump a lot in the simulation.

winds = load_file()[0]

def get_rock(rock_index, y):
    if rock_index % 5 == 0:
        return set([(2, y), (3, y), (4, y), (5, y)])
    elif rock_index % 5 == 1:
        return set([(3, y + 2), (2, y + 1), (3, y + 1), (4, y + 1), (3, y)])
    elif rock_index % 5 == 2:
        return set([(2, y), (3, y), (4, y), (4, y + 1), (4, y + 2)])
    elif rock_index % 5 == 3:
        return set([(2, y), (2, y + 1),(2, y + 2),(2, y + 3)])
    elif rock_index % 5 == 4:
        return set([(2, y + 1), (2, y), (3, y + 1), (3, y)])

def move_rock_left(rock):
    if any([x == 0 for (x, _) in rock]):
        return rock
    return set([(x-1, y) for (x, y) in rock])

def move_rock_right(rock):
    if any([x == 6 for (x, _) in rock]):
        return rock
    return set([(x + 1, y) for (x, y) in rock])

def move_rock_down(rock):
    return set([(x, y - 1) for (x, y) in rock])

def move_rock_up(rock):
    return set([(x, y + 1) for (x, y) in rock])

def show_pile(rock_pile):
    string = ""
    for y in range(max([y for (_, y) in rock_pile]),0,-1):
        for x in range(7):
            if (x, y) in rock_pile:
                string += '#'
            else:
                string += ' '
        string += string
    print(string)

def rock_pile_signature(rock_pile):
    n_top_rows = 20 # 16 -> 17 was the first time the answer didn't change. So let's use 20 for safety's sake.
    max_y = max([y for (_, y) in rock_pile])
    # We use a frozen set to be able to use it as a dict key
    return frozenset([(x, max_y-y) for (x, y) in rock_pile if max_y - y <= n_top_rows])

def simulate(n_rocks):
    rock_pile = set([(x, 0) for x in range(7)])

    seen_combinations = dict()
    top_rock_index = 0
    wind_index = 0
    rock_index = 0
    wind_cycle_length = len(winds)
    height_skipped = 0
    n_non_skipped_rocks = 0
    repeating_after = -1

    while rock_index < n_rocks:
        rock = get_rock(rock_index, top_rock_index + 4)
        rock_falling = True
        while rock_falling:
            if winds[wind_index] == "<":
                rock = move_rock_left(rock)
                if rock & rock_pile:
                    rock = move_rock_right(rock)
            else:
                rock = move_rock_right(rock)
                if rock & rock_pile:
                    rock = move_rock_left(rock)

            wind_index = (wind_index + 1) % wind_cycle_length

            rock = move_rock_down(rock)

            if rock & rock_pile:
                rock_falling = False
                rock = move_rock_up(rock)
                rock_pile = rock_pile | rock
                top_rock_index = max([y for (_, y) in rock_pile])

                combination = (wind_index, rock_index % 5, rock_pile_signature(rock_pile))
                
                # If we already have seen the current combination, we can skip ahead as many rocks as it is possible to fit
                # in the remaining rocks
                if combination in seen_combinations:
                    # Calculate what has happened since the last time we were in this position
                    (previous_rock_index, previous_top_rock_index) = seen_combinations[combination]
                    top_rock_index_change = top_rock_index - previous_top_rock_index
                    rock_index_change = rock_index - previous_rock_index

                    # Calculate how many cycles we can skip
                    if n_skippable_cycles := ((n_rocks - rock_index) // rock_index_change):
                        # Apply the changes of one cycle that many times
                        height_skipped += n_skippable_cycles * top_rock_index_change
                        rock_index += n_skippable_cycles * rock_index_change
                        repeating_after = wind_index + wind_cycle_length

                # Keep track of the combinations we have not seen before
                else:
                    seen_combinations[combination] = (rock_index, top_rock_index)

        rock_index += 1
        n_non_skipped_rocks += 1
        
    return top_rock_index, height_skipped, n_non_skipped_rocks, repeating_after

# Part 1
print("Part 1 version 2:")
n_rocks = 2022
top_rock_index, height_skipped, _, _ = simulate(n_rocks)
print(f"\tAnswer: {top_rock_index + height_skipped}")

# Part 2
print("Part 2:")
n_rocks = int(10**12)
top_rock_index, height_skipped, n_non_skipped_rocks, repeating_after = simulate(n_rocks)
print(f"\tPattern repeated after {repeating_after} steps, so:")
print(f"\t\t- skipped simulating {n_rocks - n_non_skipped_rocks} rocks, only simulated {n_non_skipped_rocks} rocks.")
print(f"\t\t- skipped simulating {height_skipped} in height, only simulated {top_rock_index}.")
print(f"\tAnswer: {top_rock_index + height_skipped}")