import numpy as np

with open("input.txt") as file:
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
print(n_visible)