with open("1/input.txt",'r',encoding = 'utf-8') as file:
    max = -1
    current = 0
    for line in file:
        if line == "\n":
            if current > max:
                max = current
            current = 0
        else:
            current += int(line.strip("\n"))
print(max)