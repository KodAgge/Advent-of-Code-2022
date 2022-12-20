from common import load_file
from collections import deque

def mix_numbers(indexed_encrypted_numbers, times = 1):
    for _ in range(times):
        for number_index in range(len(indexed_encrypted_numbers)):   
            # Move the number to the front of the list, keeping the order
            while indexed_encrypted_numbers[0][0] != number_index:
                indexed_encrypted_numbers.append(indexed_encrypted_numbers.popleft())

            # Extract the number we want to move
            indexed_number = indexed_encrypted_numbers.popleft()
            n_pops = indexed_number[1] % len(indexed_encrypted_numbers)

            # Pop until the number can be put in the right place by putting it last
            for _ in range(n_pops):
                indexed_encrypted_numbers.append(indexed_encrypted_numbers.popleft())
            indexed_encrypted_numbers.append(indexed_number)

    mixed_numbers = [number for _, number in indexed_encrypted_numbers]

    return mixed_numbers

def find_grove_sum(mixed_numbers):
    zero_index = mixed_numbers.index(0)
    grove_sum = 0
    for offset in [1000, 2000, 3000]:
        grove_sum += mixed_numbers[(zero_index + offset) % len(mixed_numbers)]

    return grove_sum
    
encrypted_numbers = list(map(int, load_file(test = False)))

# Part 1
indexed_encrypted_numbers = deque(list(enumerate(encrypted_numbers)))
mixed_numbers = mix_numbers(indexed_encrypted_numbers)
grove_sum = find_grove_sum(mixed_numbers)
print(f"Answer part 1: {grove_sum}")

# Part 2
decryption_key = 811589153
indexed_encrypted_numbers = deque(list(enumerate([number * decryption_key for number in encrypted_numbers])))
mixed_numbers = mix_numbers(indexed_encrypted_numbers, times=10)
grove_sum = find_grove_sum(mixed_numbers)
print(f"Answer part 2: {grove_sum}")