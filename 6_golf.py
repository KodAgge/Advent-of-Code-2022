from common import exec_stats_multi

day = 6
file_name = '"inputs/6.in"'

# Part 1
part = 1
code = [
    rf'print([[len(set([*l[i-4:i]]))for i in range(4,len(l))]for l in open({file_name})][0].index(4)+4)'
]
exec_stats_multi(code_list=code, day=day, part=part, file_name=file_name)

# Part 2
part = 2
code = [
    rf'print([[len(set([*l[i-14:i]]))for i in range(14,len(l))]for l in open({file_name})][0].index(14)+14)'
]
exec_stats_multi(code_list=code, day=day, part=part, file_name=file_name)