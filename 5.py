# Part 1
with open("5.in") as file:
    piles = [[] for _ in range(9)]
    indices = [i for i in range(1, 36, 4)]
    read_piles = True
    for line in file:
        if not read_piles:
            _, n_boxes, _, from_pile, _, to_pile = line.split()
            n_boxes, from_pile, to_pile = map(int, [n_boxes, from_pile, to_pile])
            for _ in range(n_boxes):
                piles[to_pile-1].append(piles[from_pile-1].pop())
        else:
            if line =="\n":
                read_piles = False
                piles = [pile[::-1] for pile in piles]
            else:
                for j,ind in enumerate(indices):
                    if line[ind] != " " and line[ind] > "9":
                        piles[j].append(line[ind])
    top_boxes = "".join([pile[-1] for pile in piles])
print(f"Answer part 1: {top_boxes}")

# Part 2
with open("5.in") as file:
    piles = [[] for _ in range(9)]
    indices = [i for i in range(1, 36, 4)]
    read_piles = True
    for line in file:
        if not read_piles:
            _, n_boxes, _, from_pile, _, to_pile = line.split()
            n_boxes, from_pile, to_pile = map(int, [n_boxes, from_pile, to_pile])
            boxes_to_move = []
            for _ in range(n_boxes):
                boxes_to_move.append(piles[from_pile-1].pop())
            for box in boxes_to_move[::-1]:
                piles[to_pile-1].append(box)
        else:
            if line =="\n":
                read_piles = False
                piles = [pile[::-1] for pile in piles]
            else:
                for j,ind in enumerate(indices):
                    if line[ind] != " " and line[ind] > "9":
                        piles[j].append(line[ind])
    top_boxes = "".join([pile[-1] for pile in piles])
print(f"Answer part 2: {top_boxes}")