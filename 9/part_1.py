import numpy as np

with open("input.txt") as file:
    tail_positions = set()
    h_position = [0, 0]
    t_position = [0, 0]
    for line in file:
        direction, steps = line.strip().split()
        for i in range(int(steps)):
            # Move head
            if direction == "R":
                h_position[0] += 1
            if direction == "L":
                h_position[0] -= 1
            if direction == "U":
                h_position[1] += 1
            if direction == "D":
                h_position[1] -= 1

            # Move tail
            x_diff = h_position[0] - t_position[0]
            y_diff = h_position[1] - t_position[1]
            if abs(x_diff) + abs(y_diff) > 2:
                t_position[0] += np.sign(x_diff)
                t_position[1] += np.sign(y_diff)
            elif abs(x_diff) > 1:
                t_position[0] += np.sign(x_diff)
            elif abs(y_diff) > 1:
                t_position[1] += np.sign(y_diff)

            # Save position
            tail_positions.add(str(t_position))
    print(len(tail_positions))