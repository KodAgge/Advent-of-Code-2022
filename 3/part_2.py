# Alternative 1
with open("3/input.txt",'r',encoding = 'utf-8') as file:
    total_priority = 0
    group_items = []
    for i, line in enumerate(file):
        items = line.strip()
        group_items.append(set(items))
        if i % 3 == 2:
            badge = group_items[0].intersection(group_items[1]).intersection(group_items[2]).pop()
            total_priority += ord(badge) - (96 if badge.islower() else 38)
            group_items = []
print(total_priority)

# Alternative 2
print(sum([ord(badge) - (96 if badge.islower() else 38) for badge in [set(open("3/input.txt",'r',encoding = 'utf-8').readlines()[ind[0]].strip()).intersection(set(open("3/input.txt",'r',encoding = 'utf-8').readlines()[ind[1]].strip())).intersection(set(open("3/input.txt",'r',encoding = 'utf-8').readlines()[ind[2]].strip())).pop() for ind in [(i, i + 1, i + 2) for i in range(0, len(open("3/input.txt",'r',encoding = 'utf-8').readlines()), 3)]]]))