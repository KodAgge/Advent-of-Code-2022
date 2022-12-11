from common import exec_stats_multi

day = 8
file_name = '"inputs/8.in"'

# Part 1
part = 1
code = [
    rf'print([np.sum([[min([max(grid[i,:j]),max(grid[i,j+1:]),max(grid[:i,j]),max(grid[i+1:,j])])<grid[i,j]for i in range(1,grid.shape[0]-1)]for j in range(1,grid.shape[1]-1)])+2*sum(grid.shape)-4 for grid in[np.array([list(map(int,list(line.strip())))for line in open({file_name})])]][0])'
]
exec_stats_multi(code_list=code, day=day, part=part, file_name=file_name)