class Monkey():

    def __init__(
        self,
        monkey_number,
        starting_items,
        operation,
        divisible,
        monkey_true,
        monkey_false,
        part,
        worry_denominator = 1,
        worry_modulo = 1
    ) -> None:
        self.number = monkey_number
        self.items = starting_items
        self.divisible = divisible
        self.monkey_true = monkey_true
        self.monkey_false = monkey_false
        self.part = part
        self.operation = operation
        self.inspected_items = 0
        self.worry_denominator = worry_denominator
        self.worry_modulo = worry_modulo

    def inspect_parser(self, item):
        self.inspected_items += 1
        # print(f"\tMonkey inspects an item with a worry level of {item}.")
        _, operator, number = self.operation.split()
        if operator == "+":
            addition = item if number == "old" else int(number)
            item += addition
            # print(f"\t\tWorry level is increased by {addition} to {item}.")
        elif operator == "*":
            factor = item if number == "old" else int(number)
            item *= factor
            # print(f"\t\tWorry level is multiplied by {factor} to {item}.")
        if self.part == 1:
            item = item // self.worry_denominator
            # print(f"\t\tMonkey gets bored with item. Worry level is divided by {self.worry_denominator} to {item}.")
        elif self.part == 2:
            item = item % self.worry_modulo
            # print(f"\t\tMonkey gets bored with item. Worry level is moduloed by {self.worry_modulo} to {item}.")
        return item

    def inspect(self, item):
        self.inspected_items += 1
        item = eval(self.operation.replace("old", "item"))
        if self.part == 1:
            item = item // self.worry_denominator
            # print(f"\t\tMonkey gets bored with item. Worry level is divided by {self.worry_denominator} to {item}.")
        elif self.part == 2:
            item = item % self.worry_modulo
            # print(f"\t\tMonkey gets bored with item. Worry level is moduloed by {self.worry_modulo} to {item}.")
        return item
    
    def throw(self):
        item = self.items.pop(0)
        item = self.inspect(item)
        if item % self.divisible:
            # print(f"\t\tCurrent worry level is not divisible by {divisible}.")
            # print(f"\t\tItem with worry level {item} is thrown to monkey {self.monkey_false}.")
            return self.monkey_false, item
        # print(f"\t\tCurrent worry level is divisible by {divisible}.")
        # print(f"\t\tItem with worry level {item} is thrown to monkey {self.monkey_true}.")
        return self.monkey_true, item

def print_monkeys(monkeys, round):
    print(f"After round {round+1}")
    for monkey in monkeys:
        print(f"Monkey {monkey.number}: {monkey.items}")

def parse_file(part, worry_denominator=3, worry_modulo=1):
    with open(file_name) as file:
        lines = file.readlines()
        monkeys = []
        for i in range(0,len(lines),7):
            monkey_number = int(lines[i][7:].strip(":\n"))
            starting_items = list(map(int, lines[i+1][18:].strip().split(", ")))
            operation = lines[i+2][19:].strip()
            divisible = int(lines[i+3][21:].strip())
            monkey_true = int(lines[i+4][28:].strip())
            monkey_false = int(lines[i+5][29:].strip())
            monkeys.append(Monkey(monkey_number=monkey_number, starting_items=starting_items, 
                                    operation=operation, part=part,
                                    divisible=divisible, monkey_true=monkey_true, 
                                    monkey_false=monkey_false, worry_denominator=worry_denominator,
                                    worry_modulo=worry_modulo))
    return monkeys

def get_modulo():
    with open(file_name) as file:
        lines = file.readlines()
        modulo = 1
        for i in range(0,len(lines),7):
            modulo *= int(lines[i+3][21:].strip())
    return modulo

def simulate_rounds(monkeys, n_rounds):
    for _ in range(n_rounds):
        for monkey in monkeys:
            # print(f"Monkey {monkey.number}:")
            while len(monkey.items) > 0:
                receiving_monkey, item = monkey.throw()
                monkeys[receiving_monkey].items.append(item)
    n_throws = [monkey.inspected_items for monkey in monkeys]
    n_throws_sorted = sorted(n_throws)
    return n_throws_sorted[-1]*n_throws_sorted[-2]

file_name = "inputs/11.in"

# Part 1
monkeys = parse_file(part=1, worry_denominator=3)
print(f"Answer part 1: {simulate_rounds(monkeys, 20)}")

# Part 2
worry_modulo = get_modulo()
monkeys = parse_file(part=2, worry_modulo=worry_modulo)
print(f"Answer part 2: {simulate_rounds(monkeys, 10_000)}")