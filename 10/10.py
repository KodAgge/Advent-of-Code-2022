# Part 1
with open("10.in") as file:
    x = 1
    stored_values = [0]
    total_signal_strength = 0
    lines = file.readlines()
    for i in range(220):
        if i < len(lines):
            instruction = lines[i].strip()
        added_value = stored_values.pop(0)
        x += added_value
        stored_values.append(0)
        if instruction[:4] == "addx":
            stored_values.append(int(instruction.split()[1]))
        if (i+1-20) % 40 == 0:
            total_signal_strength += (i+1) * x
    print(total_signal_strength)

# Part 2
import time

with open("10.in") as file:
    x = 1
    stored_values = [0]
    total_signal_strength = 0
    lines = file.readlines()
    string = ""
    for i in range(240):
        if i < len(lines):
            instruction = lines[i].strip()
        added_value = stored_values.pop(0)
        x += added_value
        stored_values.append(0)
        if instruction[:4] == "addx":
            stored_values.append(int(instruction.split()[1]))
        if x-1 <= i%40 <= x+1:
            string += "██"
        else:
            string += "  "
        if (i+1) % 40 == 0:
            string += "\n"
    print(string)

for c in string:
    print(c, end='')
    time.sleep(0.01)