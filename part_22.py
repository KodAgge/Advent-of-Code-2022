with open("2/input.txt",'r',encoding = 'utf-8') as file:
    score = 0
#     for line in file:
#         opp, me = line.strip().split()
        # score += (ord(me)-ord("X"))*3
#         (ord("Y")-89)*3
# #         if me == "Y":
# #             if opp == "A":
# #                 score += 4
# #             if opp == "B":
# #                 score += 5
# #             if opp == "C":
# #                 score += 6
# #         elif me == "X":
# #             if opp == "A":
# #                 score += 3
# #             if opp == "B":
# #                 score += 1
# #             if opp == "C":
# #                 score += 2
# #         else:
# #             if opp == "A":
# #                 score += 8
# #             if opp == "B":
# #                 score += 9
# #             if opp == "C":
# #                 score += 7
# print(score)
result = (ord("X")-ord("Y"))

# choice = chr(ord("Z") + result)
# print(choice)
print(ord("X") - ord("A"))