from common import exec_stats_multi

day = 2
file_name = '"inputs/2.in"'

# Part 1
part = 1
code = [
    rf'print(sum([(6 if ord(m[0])-ord(m[1])in[-21,-24]else(3 if ord(m[0])-ord(m[1])==-23 else 0))+ord(m[1])-87 for m in[l.strip().split()for l in open({file_name})]]))',
    rf'print(sum([(6 if ord(o)-ord(m)in[-21,-24]else(3 if ord(o)-ord(m)==-23 else 0))+ord(m)-87 for o,_,m,_ in open({file_name})]))',
    rf'print(sum((ord(m)-ord(o)+2)%3*3-87+ord(m)for o,_,m,_ in open({file_name})))'
]
exec_stats_multi(code_list=code, day=day, part=part, file_name=file_name)


# Part 2
part = 2
code = [
    rf'print(sum([((ord(m[1])-88)*3)+(ord(m[0])+(ord(m[1])-89)*(1-(3 if(ord(m[1])-ord(m[0])==23)else 0))-64)for m in[l.strip().split()for l in open({file_name})]]))',
    rf'print(sum(((ord(m)-88)*3)+(ord(o)+(ord(m)-89)*(1-(3 if(ord(m)-ord(o)==23)else 0))-64) for o,_,m,_ in open({file_name})))',
    rf'print(sum(ord(m)*3-263+(ord(o)-1+ord(m))%3 for o,_,m,_ in open({file_name})))'
]
exec_stats_multi(code_list=code, day=day, part=part, file_name=file_name)