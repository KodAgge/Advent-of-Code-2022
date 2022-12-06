with open("input.txt") as file:
    for line in file:
        for i in range(14,len(line)):
            if len(set([*line[i-14:i]])) == 14:
                print(i)
                break