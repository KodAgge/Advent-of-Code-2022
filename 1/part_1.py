# ALternative 1
with open("input.txt",'r',encoding = 'utf-8') as file:
    max_ = -1
    current = 0
    for line in file:
        if line == "\n":
            if current > max_:
                max_ = current
            current = 0
        else:
            current += int(line.strip("\n"))
print(max_)

# Alternative 2
print(max([sum([int(s)for s in e.split()])for e in"".join(["," if l=="\n" else l.strip()+" "for l in open("input.txt",'r',encoding='utf-8')]).split(",")]))

# Alternative 3
print(max(sum(int(s)for s in e.split())for e in"".join([","if l=="\n"else l[:-1]+" "for l in open("i")]).split(",")))