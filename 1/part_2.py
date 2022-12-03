# Alternative 1
with open("1/input.txt",'r',encoding = 'utf-8') as file:
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
print(sum(sorted([sum([int(snack) for snack in elf.split()]) for elf in "".join(["," if line == "\n" else line.strip() + " " for line in open("1/input.txt",'r',encoding = 'utf-8').readlines()]).split(",")], reverse=True)[:3]))