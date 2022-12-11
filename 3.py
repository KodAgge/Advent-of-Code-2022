# Part 1
with open("inputs/3.in") as file:
    total_priority = 0
    for line in file:
        items = line.strip()
        item = set(items[:len(items)//2]).intersection(set(items[len(items)//2:])).pop()
        total_priority += ord(item) - (96 if item.islower() else 38)
print(f"Answer part 1: {total_priority}")

# Part 2
with open("inputs/3.in") as file:
    total_priority = 0
    group_items = []
    for i, line in enumerate(file):
        items = line.strip()
        group_items.append(set(items))
        if i % 3 == 2:
            badge = group_items[0].intersection(group_items[1]).intersection(group_items[2]).pop()
            total_priority += ord(badge) - (96 if badge.islower() else 38)
            group_items = []
print(f"Answer part 2: {total_priority}")