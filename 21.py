from common import load_file
from collections import deque
from sympy import symbols, solve

read_lines = [line.strip().replace(":", " =") for line in load_file(test=False)]

# Part 1
monkey_queue = deque(read_lines)
evaluated_monkeys = set()

while monkey_queue:
    formula = monkey_queue.popleft()
    if formula.split()[2].isnumeric():
        exec(formula)
        evaluated_monkeys.add(formula.split()[0])
    else:
        _, _, monkey1, _, monkey2 = formula.split()
        if monkey1 in evaluated_monkeys and monkey2 in evaluated_monkeys:
            exec(formula)
            evaluated_monkeys.add(formula.split()[0])
        else:
            monkey_queue.append(formula)

print(f"Answer part 1: {int(root)}")


# Part 2
# First find if root monkey 1 or 2 can be calulated without the human
# and remove the human from the list
formulas = read_lines.copy()
for formula in formulas:
    if formula[:4] == "root":
        _, _, root_monkey1, _, root_monkey2 = formula.split()
    if formula[:4] == "humn":
        formulas.remove(formula)

# Save the formulas in a dict with monkey name as dict
# Also save the monkeys needed to calculate the formula for every monkey
monkey_dict = {}
formula_dict = {}
for formula in formulas:
    if len(formula.split()) > 3:
        monkey_dict[formula.split()[0]] = [formula.split()[2], formula.split()[4]]
    else:
        monkey_dict[formula.split()[0]] = [formula.split()[2]]
    formula_dict[formula.split()[0]] = "(" + formula[7:] + ")"

monkey_queue = deque(formulas)
evaluated_monkeys = set()

# Find the monkey that we need to much to the known number
while monkey_queue:
    if root_monkey1 in evaluated_monkeys:
        calculated_match_monkey = root_monkey1
        match_monkey = root_monkey2
        break
    elif root_monkey2 in evaluated_monkeys:
        calculated_match_monkey = root_monkey2
        match_monkey = root_monkey1
        break
    formula = monkey_queue.popleft()
    if formula.split()[2].isnumeric():
        exec(formula)
        evaluated_monkeys.add(formula.split()[0])
    else:
        monkey, _, monkey1, _, monkey2 = formula.split()
        if monkey1 in evaluated_monkeys and monkey2 in evaluated_monkeys:
            exec(formula)
            evaluated_monkeys.add(formula.split()[0])
        else:
            monkey_queue.append(formula)


# Get the formula for the thing we need to match in terms of humn,
# e.g. match = 1 + 3 / (4 + humn)
calculation_queue = deque([match_monkey])
total_formula = formula_dict[match_monkey]
while calculation_queue:
    monkey = calculation_queue.popleft()
    if monkey == "humn":
        continue
    total_formula = total_formula.replace(monkey, formula_dict[monkey])
    for term in monkey_dict[monkey]:
        if term.isnumeric():
            continue
        calculation_queue.append(term)

# Solve for humn
total_formula += " - " + str(int(eval(calculated_match_monkey)))
humn = symbols("humn")
expr = eval(total_formula)
print("Part 2:")
print(f"\tThe expression to solve for simplifies to {expr} = 0")
sol = solve(expr)
print(f"\tWhich gives the solution {int(sol[0])}")