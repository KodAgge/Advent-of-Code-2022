class Tree:
    def __init__(self, name = "/", parent = None):
        self.parent = parent
        self.name = name
        self.children = []
        self.storage = 0

    def __repr__(self) -> str:
        return f"name: {self.name}, children: {self.children}"

all_dirs = []

def get_all_dirs(node):
    for child in node.children:
        get_all_dirs(child)
    all_dirs.append(node.storage)


def sum_sub_tree(node):
    for child in node.children:
        node.storage += sum_sub_tree(child)
    return node.storage

def print_tree(node, depth = 0):
    print('\t'*depth, node.name, node.storage)
    for child in node.children:
        print_tree(child, depth + 1)

with open("input.txt") as file:
    root = Tree()
    cwd = root
    read_mode = False
    for line in file:
        inputs = line.strip().split()
        if inputs[0] == "$" and inputs[1] == "cd" and inputs[2] == "/":
            cwd = root
        elif inputs[0] == "$" and inputs[1] == "cd" and inputs[2] == "..":
            cwd = cwd.parent
        elif inputs[0] == "$" and inputs[1] == "cd" and inputs[2] != "/":
            index = [dir.name for dir in cwd.children].index(inputs[2])
            cwd = cwd.children[index]
        elif inputs[0] == "$" and inputs[1] == "ls":
            read_mode = True
        elif read_mode and inputs[0] == "dir":
            if inputs[1] not in [dir.name for dir in cwd.children]:
                cwd.children.append(Tree(name=inputs[1], parent=cwd))
        elif read_mode and inputs[0].isdigit():
            cwd.storage += int(inputs[0])
        elif read_mode and inputs[0] == "$":
            read_mode = False



print_tree(root)
sum_sub_tree(root)
print_tree(root)
get_all_dirs(root)
# print(sorted(all_dirs))
available = 70_000_000 - max(all_dirs)
print(available)
sorted_all_dirs = sorted(all_dirs)
for dir in sorted_all_dirs:
    if available + dir >= 30_000_000:
        print(dir)
        break