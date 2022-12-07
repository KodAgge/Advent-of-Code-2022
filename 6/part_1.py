# Alternative 1
with open("input.txt") as file:
    for line in file:
        for i in range(4,len(line)):
            if len(set([*line[i-4:i]])) == 4:
                print(i)
                break

# Alternative 2
print([[len(set([*l[i-4:i]]))for i in range(4,len(l))]for l in open("i")][0].index(4)+4)