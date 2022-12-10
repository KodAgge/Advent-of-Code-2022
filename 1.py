# Part 1
with open("1.in") as file:
    max_ = -1
    current = 0
    for line in file:
        if line == "\n":
            if current > max_:
                max_ = current
            current = 0
        else:
            current += int(line.strip("\n"))
print(f"Answer part 1: {max_}")

# Part 2
with open("1.in") as file:
    snack_sum_list = []
    current = 0
    for line in file:
        if line == "\n":
            snack_sum_list.append(current)
            current = 0
        else:
            current += int(line.strip("\n"))
snack_sum_list.sort(reverse=True)
print(f"Answer part 2: {sum(snack_sum_list[:3])}")