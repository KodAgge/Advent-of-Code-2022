import numpy as np

# Part 1
with open("inputs/8.in") as file:
    matrix = []
    for line in file:
        matrix.append(list(map(int, list(line.strip()))))

grid = np.array(matrix)
w, h = grid.shape
n_visible = 2 * (w + h) - 4

for i in range(1,w-1):
    for j in range(1,h-1):
        tree_height = grid[i,j]
        n_visible += np.max(grid[i,:j]) < tree_height or \
                        np.max(grid[i,j+1:]) < tree_height or \
                            np.max(grid[:i,j]) < tree_height or  \
                                np.max(grid[i+1:,j]) < tree_height
print(f"Answer part 1: {n_visible}")

# Part 2
scenic_scores = np.zeros(grid.shape)

for i in range(h-1):
    for j in range(w-1):
        tree_height = grid[i,j]

        # Up
        up = grid[:i,j]
        blocking = up >= tree_height
        first_blocking_tree = np.where(blocking == True)[0]
        n_trees_up = len(up) - (first_blocking_tree[-1] if len(first_blocking_tree) > 0 else 0)

        # Down
        down = grid[i+1:,j]
        blocking = down >= tree_height
        first_blocking_tree = np.where(blocking == True)[0]
        n_trees_down = len(down) - (len(down) - first_blocking_tree[0] - 1 if len(first_blocking_tree) > 0 else 0)

        # Left
        left = grid[i,:j]
        blocking = left >= tree_height
        first_blocking_tree = np.where(blocking == True)[0]
        n_trees_left = len(left) - (first_blocking_tree[-1] if len(first_blocking_tree) > 0 else 0)

        # Right
        right = grid[i,j+1:]
        blocking = right >= tree_height
        first_blocking_tree = np.where(blocking == True)[0]
        n_trees_right = len(right) - (len(right) - first_blocking_tree[0] - 1 if len(first_blocking_tree) > 0 else 0)

        # Save 
        scenic_scores[i,j] += n_trees_up*n_trees_down*n_trees_left*n_trees_right

print(f"Answer part 2: {int(np.max(scenic_scores))}")