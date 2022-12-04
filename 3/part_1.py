# Alternative 1
with open("input.txt",'r',encoding = 'utf-8') as file:
    total_priority = 0
    for line in file:
        items = line.strip()
        item = set(items[:len(items)//2]).intersection(set(items[len(items)//2:])).pop()
        total_priority += ord(item) - (96 if item.islower() else 38)
print(total_priority)

# Alternative 2
print(sum([ord(set(l.strip()[:len(l.strip())//2]).intersection(set(l.strip()[len(l.strip())//2:])).pop())-(96 if set(l.strip()[:len(l.strip())//2]).intersection(set(l.strip()[len(l.strip())//2:])).pop().islower() else 38) for l in open("input.txt",'r',encoding='utf-8')]))

# Alternative 3
print(sum([ord(b)-(96 if b.islower()else 38)for b in[set(l[:len(l)//2]).intersection(set(l[len(l)//2:])).pop()for l in[u.strip()for u in open("input.txt",'r',encoding='utf-8')]]]))

# Alternative 4
print(sum(ord(b)%32+26*(ord(b)<97)for b in[set(l[:len(l)//2]).intersection(set(l[len(l)//2:])).pop()for l in[u.strip()for u in open("i")]]))

# Alternative 5
print(sum(ord(b)%32+26*(ord(b)<97)for b in[set(l[:len(l)//2]).intersection(set(l[len(l)//2:])).pop()for l in open("i")]))

# Alternative 6
print(sum(ord(b)%32+26*(ord(b)<97)for b in[(set(l[:len(l)//2])&set(l[len(l)//2:])).pop()for l in open("i")]))