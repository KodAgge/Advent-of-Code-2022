from common import exec_stats_multi

day = 1
file_name = "1.in"

# Part 1
part = 1
code = [
    r'print(max([sum([int(s)for s in e.split()])for e in"".join(["," if l=="\n" else l.strip()+" "for l in open("1.in")]).split(",")]))',
    r'print(max(sum(int(s)for s in e.split())for e in"".join([","if l=="\n"else l.strip()+" "for l in open("1.in")]).split(",")))'
]
exec_stats_multi(code_list=code, day=day, part=part, file_name=file_name)


# Part 2
part = 2
code = [
    r'print(sum(sorted([sum([int(s)for s in e.split()])for e in"".join(["," if l=="\n" else l.strip()+" "for l in open("1.in")]).split(",")],reverse=1)[:3]))',
    r'print(sum(sorted([sum(int(s)for s in e.split())for e in"".join(","if l=="\n"else l.strip()+" "for l in open("1.in")).split(",")],reverse=1)[:3]))'
]
exec_stats_multi(code_list=code, day=day, part=part, file_name=file_name)