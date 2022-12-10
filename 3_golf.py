from common import exec_stats_multi

day = 3
file_name = "3.in"

# Part 1
part = 1
code = [
    r'print(sum([ord(set(l.strip()[:len(l.strip())//2]).intersection(set(l.strip()[len(l.strip())//2:])).pop())-(96 if set(l.strip()[:len(l.strip())//2]).intersection(set(l.strip()[len(l.strip())//2:])).pop().islower() else 38) for l in open("3.in")]))',
    r'print(sum([ord(b)-(96 if b.islower()else 38)for b in[set(l[:len(l)//2]).intersection(set(l[len(l)//2:])).pop()for l in[u.strip()for u in open("3.in")]]]))',
    r'print(sum(ord(b)%32+26*(ord(b)<97)for b in[set(l[:len(l)//2]).intersection(set(l[len(l)//2:])).pop()for l in[u.strip()for u in open("3.in")]]))',
    r'print(sum(ord(b)%32+26*(ord(b)<97)for b in[set(l[:len(l)//2]).intersection(set(l[len(l)//2:])).pop()for l in open("3.in")]))',
    r'print(sum(ord(b)%32+26*(ord(b)<97)for b in[(set(l[:len(l)//2])&set(l[len(l)//2:])).pop()for l in open("3.in")]))'
]
exec_stats_multi(code_list=code, day=day, part=part, file_name=file_name)

# Part 2
part = 2
code = [
    r'print(sum([ord(b)-(96 if b.islower()else 38)for b in[[set(f[i].strip()).intersection(set(f[i+1].strip())).intersection(set(f[i+2].strip())).pop()for i in range(0,len(f),3)]for f in[open("3.in").readlines()]][0]]))',
    r'print(sum(ord(b)%32+26*(ord(b)<97)for b in[[(a&b&c).pop()for(a,b,c)in zip(f[::3],f[1::3],f[2::3])]for f in[[set(l.strip())for l in open("3.in")]]][0]))',
    r'print(sum(ord(b)%32+26*(ord(b)<97)for b in[[(f[i]&f[i+1]&f[i+2]).pop()for i in range(0,len(f),3)]for f in[[set(l.strip())for l in open("3.in")]]][0]))'
]
exec_stats_multi(code_list=code, day=day, part=part, file_name=file_name)