# Alternative 1
with open("input.txt",'r',encoding = 'utf-8') as file:
    snack_sum_list = []
    current = 0
    for line in file:
        if line == "\n":
            snack_sum_list.append(current)
            current = 0
        else:
            current += int(line.strip("\n"))
snack_sum_list.sort(reverse=True)
print(sum(snack_sum_list[:3]))

# Alternative 2
print(sum(sorted([sum([int(s)for s in e.split()])for e in"".join(["," if l=="\n" else l.strip()+" "for l in open("input.txt",'r',encoding='utf-8')]).split(",")],reverse=1)[:3]))

# Alternative 3
print(sum(sorted([sum(int(s)for s in e.split())for e in"".join(","if l=="\n"else l[:-1]+" "for l in open("i")).split(",")],reverse=1)[:3]))