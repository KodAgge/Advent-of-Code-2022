class Tree:
    def __init__(self, name = "/", parent = None):
        self.parent = parent
        self.name = name
        self.children = []
        self.storage = 0

    def __repr__(self) -> str:
        return f"name: {self.name}, children: {self.children}"

small_dirs = []
NODE_CUTOFF = 100000

def get_small_dirs(node):
    for child in node.children:
        get_small_dirs(child)
    if node.storage <= NODE_CUTOFF:
        small_dirs.append(node.storage)

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

sum_sub_tree(root)
get_small_dirs(root)
print(sum(small_dirs))