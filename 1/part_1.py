# ALternative 1
with open("1/input.txt",'r',encoding = 'utf-8') as file:
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
print(max([sum([int(snack) for snack in elf.split()]) for elf in "".join(["," if line == "\n" else line.strip() + " " for line in open("1/input.txt",'r',encoding = 'utf-8').readlines()]).split(",")]))