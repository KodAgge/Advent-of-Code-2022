# Part 1
with open("2.in") as file:
    score = 0
    for line in file:
        opp, me = line.strip().split()
        score += (6 if ord(opp) - ord(me) in [-21, -24] else (3 if ord(opp) - ord(me) == -23 else 0)) + (1 if me == "X" else (2 if me == "Y" else 3))
print(f"Answer part 1: {score}")

# Part 2
# Alternative 1
with open("2.in") as file:
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
print(f"Answer part 2 v1: {score}")

# Alternative 2
with open("2.in") as file:
    score = 0
    for line in file:
        opp, me = line.strip().split()
        match_result = (ord(me) - ord("X")) * 3
        points_of_choice = ord(opp) + (ord(me)-ord("Y")) * (1 - (3 if (ord(me) - ord(opp) == 23) else 0)) - 64
        score += match_result + points_of_choice
print(f"Answer part 2 v2: {score}")

# Alternative 2
print(sum([(6 if ord(m[0])-ord(m[1])in[-21,-24]else(3 if ord(m[0])-ord(m[1])==-23 else 0))+ord(m[1])-87 for m in[l.strip().split()for l in open("2.in")]]))

# Alternative 3
print(sum([(6 if ord(o)-ord(m)in[-21,-24]else(3 if ord(o)-ord(m)==-23 else 0))+ord(m)-87 for o,_,m,_ in open("2.in")]))

# Alternative 4
print(sum((ord(m)-ord(o)+2)%3*3-87+ord(m)for o,_,m,_ in open("2.in")))