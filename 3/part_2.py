# Alternative 1
with open("input.txt",'r',encoding = 'utf-8') as file:
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
print(sum([ord(b)-(96 if b.islower()else 38)for b in[[set(f[i].strip()).intersection(set(f[i+1].strip())).intersection(set(f[i+2].strip())).pop()for i in range(0,len(f),3)]for f in[open("input.txt",'r',encoding='utf-8').readlines()]][0]]))

# Alternative 3
print(sum(ord(b)%32+26*(ord(b)<97)for b in[[(a&b&c).pop()for(a,b,c)in zip(f[::3],f[1::3],f[2::3])]for f in[[set(l.strip())for l in open("i")]]][0]))

# Alternative 4
print(sum(ord(b)%32+26*(ord(b)<97)for b in[[(f[i]&f[i+1]&f[i+2]).pop()for i in range(0,len(f),3)]for f in[[set(l.strip())for l in open("i")]]][0]))