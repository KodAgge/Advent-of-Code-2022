import numpy as np

def simulate_rope(n_knots):
    with open(file_name) as file:
        tail_positions = set()
        positions = [[0, 0] for _ in range(n_knots)]
        for line in file:
            direction, steps = line.strip().split()
            for i in range(int(steps)):
                # Move head
                if direction == "R":
                    positions[0][0] += 1
                if direction == "L":
                    positions[0][0] -= 1
                if direction == "U":
                    positions[0][1] += 1
                if direction == "D":
                    positions[0][1] -= 1
                
                # Move other nots
                for i in range(1, n_knots):
                    x_diff = positions[i-1][0] - positions[i][0]
                    y_diff = positions[i-1][1] - positions[i][1]
                    if abs(x_diff) + abs(y_diff) > 2:
                        positions[i][0] += np.sign(x_diff)
                        positions[i][1] += np.sign(y_diff)
                    elif abs(x_diff) > 1:
                        positions[i][0] += np.sign(x_diff)
                    elif abs(y_diff) > 1:
                        positions[i][1] += np.sign(y_diff)

                # Save position
                tail_positions.add(str(positions[-1]))
    return len(tail_positions)

file_name = "inputs/9.in"

# Part 1
print(f"Answer part 1: {simulate_rope(n_knots=2)}")

# Part 2
print(f"Answer part 2: {simulate_rope(n_knots=10)}")