# Alternative 1
with open("2/input.txt",'r',encoding = 'utf-8') as file:
    score = 0
    for line in file:
        opp, me = line.strip().split()
        score += 6 if ord(opp) - ord(me) in [-21, -24] else (3 if ord(opp) - ord(me) == -23 else 0) + 1 if me == "X" else (2 if me == "Y" else 3)        
print(score)

# Alternative 2
print(sum([6 if ord(m[0])-ord(m[1]) in [-21,-24] else (3 if ord(m[0])-ord(m[1])==-23 else 0)+1 if m[1]=="X" else (2 if m[1]=="Y" else 3) for m in [line.strip().split() for line in open("2/input.txt",'r',encoding = 'utf-8')]]))