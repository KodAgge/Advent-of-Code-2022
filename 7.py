class Tree:
    def __init__(self, name = "/", parent = None):
        self.parent = parent
        self.name = name
        self.children = []
        self.storage = 0

    def __repr__(self) -> str:
        return f"name: {self.name}, children: {self.children}"

def get_small_dirs(node):
    for child in node.children:
        get_small_dirs(child)
    if node.storage <= NODE_CUTOFF:
        small_dirs.append(node.storage)

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

def execute_instructions():
    with open(file_name) as file:
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
    return root

file_name = "7.in"

# Part 1
small_dirs = []
NODE_CUTOFF = 100000
root = execute_instructions()
sum_sub_tree(root)
get_small_dirs(root)
print(f"Answer part 1: {sum(small_dirs)}")

# Part 2
all_dirs = []
MAX_STORAGE = 70_000_000
root = execute_instructions()
sum_sub_tree(root)
get_all_dirs(root)
available_storage = MAX_STORAGE - max(all_dirs)

for dir in sorted(all_dirs):
    if available_storage + dir >= 30_000_000:
        print(f"Answer part 1: {dir}")
        break