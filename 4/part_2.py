# Alternative 1
with open("input.txt") as file:
    overlaps = 0
    for line in file:
        e1, e2 = line.strip().split(",")
        e1_start, e1_end = map(int, e1.split("-"))
        e2_start, e2_end = map(int, e2.split("-"))
        overlaps += (e2_start <= e1_start <= e2_end or e2_start <= e1_end <= e2_end) or (e1_start <= e2_start <= e1_end or e1_start <= e2_end <= e1_end)
print(overlaps)

# Alternative 2
with open("input.txt") as file:
    overlaps = 0
    for line in file:
        e1, e2 = line.strip().split(",")
        e1_start, e1_end = map(int, e1.split("-"))
        e2_start, e2_end = map(int, e2.split("-"))
        overlaps += len(set(list(range(e1_start, e1_end + 1))) & set(list(range(e2_start, e2_end + 1)))) > 0
print(overlaps)

# Alternative 3
print(sum((len(set(list(range(a,b+1)))&set(list(range(x,y+1))))>0)for(a,b),(x,y)in[[[i for i in map(int,j.split("-"))]for j in l.strip().split(",")]for l in open("i")]))

# Alternative 4
print(sum(len(x&y)>0 for(x,y)in[[set(list(range(s,f+1)))for(s,f)in p]for p in[[[i for i in map(int,j.split("-"))]for j in l[:-1].split(",")]for l in open("i")]]))

# Alternative 5
print(sum((x<=a<=y or x<=b<=y)or(a<=x<=b or a<=y<=b)for(a,b),(x,y)in[[[i for i in map(int,j.split("-"))]for j in l[:-1].split(",")]for l in open("i")]))

# Alternative 6
print(sum(x<=a<=y or x<=b<=y or a<x<b for(a,b),(x,y)in[[[i for i in map(int,j.split("-"))]for j in l[:-1].split(",")]for l in open("i")]))