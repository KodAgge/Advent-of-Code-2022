# Alternative 1
with open("3/input.txt",'r',encoding = 'utf-8') as file:
    total_priority = 0
    for line in file:
        items = line.strip()
        item = set(items[:len(items)//2]).intersection(set(items[len(items)//2:])).pop()
        total_priority += ord(item) - (96 if item.islower() else 38)
print(total_priority)

# Alternative 2
print(sum([ord(set(l.strip()[:len(l.strip())//2]).intersection(set(l.strip()[len(l.strip())//2:])).pop())-(96 if set(l.strip()[:len(l.strip())//2]).intersection(set(l.strip()[len(l.strip())//2:])).pop().islower() else 38) for l in open("3/input.txt",'r',encoding='utf-8')]))

# Alternative 3
print(sum([ord(b)-(96 if b.islower()else 38)for b in[set(l[:len(l)//2]).intersection(set(l[len(l)//2:])).pop()for l in[u.strip()for u in open("3/input.txt",'r',encoding='utf-8')]]]))