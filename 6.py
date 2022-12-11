# Part 1
with open("inputs/6.in") as file:
    for line in file:
        for i in range(4,len(line)):
            if len(set([*line[i-4:i]])) == 4:
                print(f"Answer part 1: {i}")
                break

# Part 2
with open("inputs/6.in") as file:
    for line in file:
        for i in range(14,len(line)):
            if len(set([*line[i-14:i]])) == 14:
                print(f"Answer part 2: {i}")
                break