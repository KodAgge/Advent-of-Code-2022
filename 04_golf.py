from common import exec_stats_multi

day = 4
file_name = '"inputs/4.in"'

# Part 1
part = 1
code = [
    rf'print(sum((a>=x and b<=y)or(a<=x and b>=y)for(a,b),(x,y)in[[[i for i in map(int,j.split("-"))]for j in l.strip().split(",")]for l in open({file_name})]))',
    rf'print(sum((a>=x and b<=y)or(a<=x and b>=y)for a,b,x,y in(map(int,l.strip().replace(",","-").split("-"))for l in open({file_name}))))'
]
exec_stats_multi(code_list=code, day=day, part=part, file_name=file_name)

# Part 2
part = 2
code = [
    rf'print(sum((len(set(list(range(a,b+1)))&set(list(range(x,y+1))))>0)for(a,b),(x,y)in[[[i for i in map(int,j.split("-"))]for j in l.strip().split(",")]for l in open({file_name})]))',
    rf'print(sum(len(x&y)>0 for(x,y)in[[set(list(range(s,f+1)))for(s,f)in p]for p in[[[i for i in map(int,j.split("-"))]for j in l.strip().split(",")]for l in open({file_name})]]))',
    rf'print(sum((x<=a<=y or x<=b<=y)or(a<=x<=b or a<=y<=b)for(a,b),(x,y)in[[[i for i in map(int,j.split("-"))]for j in l.strip().split(",")]for l in open({file_name})]))',
    rf'print(sum(x<=a<=y or x<=b<=y or a<x<b for(a,b),(x,y)in[[[i for i in map(int,j.split("-"))]for j in l.strip().split(",")]for l in open({file_name})]))',
    rf'print(sum(1-(a>y or b<x)for(a,b),(x,y)in[[[i for i in map(int,j.split("-"))]for j in l.strip().split(",")]for l in open({file_name})]))',
    rf'print(sum(1-(a>y or b<x)for a,b,x,y in(map(int,l.strip().replace(",","-").split("-"))for l in open({file_name}))))'
]
exec_stats_multi(code_list=code, day=day, part=part, file_name=file_name)