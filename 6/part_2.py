# Alternative 1
with open("input.txt") as file:
    for line in file:
        for i in range(14,len(line)):
            if len(set([*line[i-14:i]])) == 14:
                print(i)
                break


# Alternative 2
print([[len(set([*l[i-14:i]]))for i in range(14,len(l))]for l in open("i")][0].index(14)+14)