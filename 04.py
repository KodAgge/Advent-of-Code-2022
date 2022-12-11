# Part 1
with open("inputs/4.in") as file:
    overlaps = 0
    for line in file:
        e1, e2 = line.strip().split(",")
        e1_start, e1_end = map(int, e1.split("-"))
        e2_start, e2_end = map(int, e2.split("-"))
        overlaps += (e1_start >= e2_start and e1_end <= e2_end) or (e1_start <= e2_start and e1_end >= e2_end)
print(f"Answer part 1: {overlaps}")

# Part 2

# Alternative 1
with open("inputs/4.in") as file:
    overlaps = 0
    for line in file:
        e1, e2 = line.strip().split(",")
        e1_start, e1_end = map(int, e1.split("-"))
        e2_start, e2_end = map(int, e2.split("-"))
        overlaps += (e2_start <= e1_start <= e2_end or e2_start <= e1_end <= e2_end) or (e1_start <= e2_start <= e1_end or e1_start <= e2_end <= e1_end)
print(f"Answer part 2 v1: {overlaps}")

# Alternative 2
with open("inputs/4.in") as file:
    overlaps = 0
    for line in file:
        e1, e2 = line.strip().split(",")
        e1_start, e1_end = map(int, e1.split("-"))
        e2_start, e2_end = map(int, e2.split("-"))
        overlaps += len(set(list(range(e1_start, e1_end + 1))) & set(list(range(e2_start, e2_end + 1)))) > 0
print(f"Answer part 2 v2: {overlaps}")