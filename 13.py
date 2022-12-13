def parse_file_part_1(file_name):
    with open(file_name) as file:
        left = []
        right = []
        for i, line in enumerate(file):
            if i % 3 == 0:
                left.append(eval(line))
            elif i % 3 == 1:
                right.append(eval(line))
    return left, right

def compare_lists(left, right):
    # If both are int, return difference in value
    if isinstance(left, int) and isinstance(right, int):
        return left - right

    # If one is int and one list, make the int a list and continue
    elif isinstance(left, int) and isinstance(right, list):
        return compare_lists([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare_lists(left, [right])
    
    # If both are lists, continue with looping through them
    # Will only loop for as many items there are in the shortest list
    for l, r in zip(left, right):
        # If right is smaller, stop looping
        if value_diff := compare_lists(l, r):
            return value_diff

    # If left is still smaller, return the difference in list length
    return len(left) - len(right)

def compare_lists_print(left, right, level = 0):
    if level == 0:
        print(f"{'  '*level}- Compare {left} vs {right}")
        level += 1

    # If both are int, return difference in value
    if isinstance(left, int) and isinstance(right, int):
        number_diff = left - right
        if number_diff > 0:
            print(f"{'  '*(level+1)}- Right side is smaller, so inputs are *not* in the right order")
        elif number_diff < 0:
            print(f"{'  '*(level+1)}- Left side is smaller, so inputs are in the right order")
        return number_diff

    # If one is int and one list, make the int a list and continue
    elif isinstance(left, int) and isinstance(right, list):
        print(f"{'  '*(level)}- Mixed types; convert left to [{left}] and retry comparison")
        print(f"{'  '*level}- Compare {[left]} vs {right}")
        return compare_lists_print([left], right, level+1)
    elif isinstance(left, list) and isinstance(right, int):
        print(f"{'  '*(level)}- Mixed types; convert right to [{right}] and retry comparison")
        print(f"{'  '*level}- Compare {left} vs {[right]}")
        return compare_lists_print(left, [right], level+1)
    
    # If both are lists, continue with looping through them
    # Will only loop for as many items there are in the shortest list
    for l, r in zip(left, right):
        print(f"{'  '*level}- Compare {l} vs {r}")
        # If right is smaller, stop looping
        if value_diff := compare_lists(l, r):
            return value_diff

    # If left is still smaller, return the difference in list length
    if length_diff := len(left) - len(right) > 0:
        print(f"{'  '*(level+1)}- Right side ran out of items, so inputs are *not* in the right order")
    elif length_diff < 0:
        print(f"{'  '*(level+1)}- Left side ran out of items, so inputs are in the right order")

    return length_diff


def get_index_sum(left, right):
    index_sum = 0
    for i, (l, r) in enumerate(zip(left, right)):
        if compare_lists(l, r) < 0:
            index_sum += i + 1
    return index_sum

def parse_file_part_2(file_name):
    with open(file_name) as file:
        packets = []
        for i, line in enumerate(file):
            if i % 3 != 2:
                packets.append(eval(line))
    return packets

def multiply_list(list):
    result = 1
    for value in list:
        result *= value
    return result

def locate_divider_packets(packets, divider_packets):
    divider_packets = sorted(divider_packets)
    divider_packet_indices = [1 for _ in divider_packets]

    for packet in packets:
        for i, divider_packet in enumerate(divider_packets):
            if compare_lists(packet, divider_packet) < 0:
                divider_packet_indices[i] += 1

    return multiply_list(divider_packet_indices)

file_name = "inputs/13.in"

# Part 1
left, right = parse_file_part_1(file_name)
print(f"Answer part 1: {get_index_sum(left, right)}")

# Part 2
packets = parse_file_part_2(file_name)
divider_packets = [[[2]], [[6]]]
print(f"Answer part 2: {locate_divider_packets(packets, divider_packets)}")