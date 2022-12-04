# Alternative 1
with open("input.txt",'r',encoding = 'utf-8') as file:
    score = 0
    for line in file:
        opp, me = line.strip().split()
        if me == "Y":
            if opp == "A":
                score += 4
            if opp == "B":
                score += 5
            if opp == "C":
                score += 6
        elif me == "X":
            if opp == "A":
                score += 3
            if opp == "B":
                score += 1
            if opp == "C":
                score += 2
        else:
            if opp == "A":
                score += 8
            if opp == "B":
                score += 9
            if opp == "C":
                score += 7
print(score)

# Alternative 2
with open("input.txt",'r',encoding = 'utf-8') as file:
    score = 0
    for line in file:
        opp, me = line.strip().split()
        match_result = (ord(me) - ord("X")) * 3
        points_of_choice = ord(opp) + (ord(me)-ord("Y")) * (1 - (3 if (ord(me) - ord(opp) == 23) else 0)) - 64
        score += match_result + points_of_choice
print(score)

# Alternative 3
print(sum([((ord(m[1])-88)*3)+(ord(m[0])+(ord(m[1])-89)*(1-(3 if(ord(m[1])-ord(m[0])==23)else 0))-64)for m in[l.strip().split()for l in open("input.txt",'r',encoding='utf-8')]]))

# Alternative 4
print(sum(((ord(m)-88)*3)+(ord(o)+(ord(m)-89)*(1-(3 if(ord(m)-ord(o)==23)else 0))-64) for o,_,m,_ in open("i")))

# Alternative 5
print(sum(ord(m)*3-263+(ord(o)-1+ord(m))%3 for o,_,m,_ in open("i")))