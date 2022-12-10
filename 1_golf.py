from common import exec_stats

day = 1
file_name = "1.in"

# Part 1
part = 1
code_p1 = []
code_p1.append(r'print(max([sum([int(s)for s in e.split()])for e in"".join(["," if l=="\n" else l.strip()+" "for l in open("1.in")]).split(",")]))')
code_p1.append(r'print(max(sum(int(s)for s in e.split())for e in"".join([","if l=="\n"else l.strip()+" "for l in open("1.in")]).split(",")))')

for i, code in enumerate(code_p1):
    exec_stats(code=code, day=day, part=part, code_version=i+1, file_name=file_name)

# Part 2
part = 2
code_p2 = []
code_p2.append(r'print(sum(sorted([sum([int(s)for s in e.split()])for e in"".join(["," if l=="\n" else l.strip()+" "for l in open("1.in")]).split(",")],reverse=1)[:3]))')
code_p2.append(r'print(sum(sorted([sum(int(s)for s in e.split())for e in"".join(","if l=="\n"else l.strip()+" "for l in open("1.in")).split(",")],reverse=1)[:3]))')

for i, code in enumerate(code_p2):
    exec_stats(code=code, day=day, part=part, code_version=i+1, file_name=file_name)