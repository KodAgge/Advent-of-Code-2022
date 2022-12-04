# Alternative 1
with open("input.txt") as file:
    overlaps = 0
    for line in file:
        e1, e2 = line.strip().split(",")
        e1_start, e1_end = map(int, e1.split("-"))
        e2_start, e2_end = map(int, e2.split("-"))
        overlaps += (e1_start >= e2_start and e1_end <= e2_end) or (e1_start <= e2_start and e1_end >= e2_end)
print(overlaps)

# Alternative 2
print(sum((a>=x and b<=y)or(a<=x and b>=y)for(a,b),(x,y)in[[[i for i in map(int,j.split("-"))]for j in l.strip().split(",")]for l in open("i")]))