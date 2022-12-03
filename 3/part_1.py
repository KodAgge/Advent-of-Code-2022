# Alternative 1
with open("3/input.txt",'r',encoding = 'utf-8') as file:
    total_priority = 0
    for line in file:
        items = line.strip()
        item = set(items[:len(items)//2]).intersection(set(items[len(items)//2:])).pop()
        total_priority += ord(item) - (96 if item.islower() else 38)
print(total_priority)

# Alternative 2
print(sum([ord(set(line.strip()[:len(line.strip())//2]).intersection(set(line.strip()[len(line.strip())//2:])).pop()) - (96 if set(line.strip()[:len(line.strip())//2]).intersection(set(line.strip()[len(line.strip())//2:])).pop().islower() else 38) for line in open("3/input.txt",'r',encoding = 'utf-8')]))