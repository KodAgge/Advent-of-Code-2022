# Alternative 1
with open("input.txt",'r',encoding = 'utf-8') as file:
    score = 0
    for line in file:
        opp, me = line.strip().split()
        score += (6 if ord(opp) - ord(me) in [-21, -24] else (3 if ord(opp) - ord(me) == -23 else 0)) + (1 if me == "X" else (2 if me == "Y" else 3))
print(score)

# Alternative 2
print(sum([(6 if ord(m[0])-ord(m[1])in[-21,-24]else(3 if ord(m[0])-ord(m[1])==-23 else 0))+ord(m[1])-87 for m in[l.strip().split()for l in open("input.txt",'r',encoding='utf-8')]]))

# Alternative 3
print(sum([(6 if ord(o)-ord(m)in[-21,-24]else(3 if ord(o)-ord(m)==-23 else 0))+ord(m)-87 for o,_,m,_ in open("i")]))

# Alternative 4
print(sum((ord(m)-ord(o)+2)%3*3-87+ord(m)for o,_,m,_ in open("i")))