from common import load_file
from time import perf_counter

read_lines = load_file()
parsed_lines = [line.strip().split() for line in read_lines]
parsed_lines = [[line[1], line[4], line[9:]] for line in parsed_lines]

rooms = []
rates = dict()
reachable_rooms = dict()

n_working_valves = 0
for room, rate, reachables in parsed_lines:
    rooms.append(room)
    rates[room] = int(rate.replace("rate=", "").strip(";"))
    reachable_rooms[room] = [r[:2] for r in reachables]
    n_working_valves += rates[room] > 0

# Part 1 version 1
print("Part 1 version 1:")
n_minutes = 30
open_valves = set()
max_released_pressure = -1
start = perf_counter()
queue = [("AA", 0, 0, open_valves, "")]
while queue:
    room, minute, released_pressure, open, previous_room = queue.pop()
    if minute < n_minutes and len(open) < n_working_valves:
        if rates[room] > 0:
            if room not in open:
                open_ = open.copy()
                open_.add(room)
                queue.append((room, minute + 1, released_pressure + rates[room] * (n_minutes - minute - 1), open_, ""))
        for chosen_room in reachable_rooms[room]:
            if chosen_room != previous_room:
                open_ = open.copy()
                queue.append((chosen_room, minute + 1, released_pressure, open_, room))
    if released_pressure > max_released_pressure:
        max_released_pressure = released_pressure

print(f"\tSolved in {perf_counter() - start:0.1f}, answer: {max_released_pressure}")
# The solution above will clearly not work for part 2, as it grows quadratically as fast
# We have to make use of a better solution, probably using a graph





# ====== NEXT ATTEMPT ======
# Reasoning: We don't actually have to keep track of all the rooms that are visited, instead all the rooms with vaults,
# that when opened, have a positive release rate.
# Thus we need to find the distance (minutes lost) between every room. E.g. AA -> BB = 1, AA -> CC = 2 (through BB).
# We can then calculate all possible routes to open vaults (not keeping track of zero release vaults) and how
# much pressure that would release.
# Then it's an easy sort to find the optimum route for part 1.
# For part 2 it's slightly harder. We then have to find combinations of routes that open distinct vaults, and then find
# the best combination of those.

def get_distances_between_rooms():
    distances_between_rooms = dict()
    for room in rooms:
        distances_between_rooms[room] = dict()
        room_queue = []
        for next_room in reachable_rooms[room]:
            room_queue.append((next_room, 1))
        while room_queue:
            next_room, distance_to_next_room = room_queue.pop(0)
            if next_room not in distances_between_rooms[room]:
                distances_between_rooms[room][next_room] = distance_to_next_room
                for room_after_next_room in reachable_rooms[next_room]:
                    room_queue.append((room_after_next_room, distance_to_next_room + 1))
    return distances_between_rooms

def generate_ways_to_open_vaults(current_room, remaining_vaults_to_open, opened_vaults, minute):
    ways_to_open_vaults = [opened_vaults]
    for next_vault in remaining_vaults_to_open:
        if (time_cost := distances_between_rooms[current_room][next_vault] + 1) < minute:
            new_opened_vaults = opened_vaults + [next_vault]
            sub_ways_to_open_vaults = generate_ways_to_open_vaults(
                next_vault, 
                {vault for vault in remaining_vaults_to_open if vault not in new_opened_vaults},
                new_opened_vaults,
                minute - time_cost
            )
            ways_to_open_vaults += sub_ways_to_open_vaults
    return ways_to_open_vaults

def calculate_released_pressures(ways_to_open_vaults, minutes):
    released_pressures = []
    for route in ways_to_open_vaults:
        time = 0
        released_pressure = 0
        current_room = "AA"
        for next_vault in route:
            if (time := time + (distances_between_rooms[current_room][next_vault] + 1)) >= minutes:
                break
            released_pressure += ((minutes - time) * rates[next_vault])
            current_room = next_vault
        released_pressures.append((released_pressure, set(route)))
    return released_pressures

# Part 1 version 2
print("Part 1 version 2:")
start = perf_counter()
distances_between_rooms = get_distances_between_rooms()
start_room = "AA"
vaults_to_open = {vault for vault in rates if rates[vault] > 0}
minutes = 30

ways_to_open_vaults = generate_ways_to_open_vaults(start_room, vaults_to_open, [], minutes)
print(f"\tThere were only {len(ways_to_open_vaults)} considerable ways for the human to open vaults in {minutes} minutes.")
released_pressures = calculate_released_pressures(ways_to_open_vaults, minutes)
max_released_pressure = max(result[0] for result in released_pressures)
print(f"\tSolved in {perf_counter() - start:0.1f}, answer: {max_released_pressure}")

# Part 2
print("Part 2:")
start = perf_counter()
distances_between_rooms = get_distances_between_rooms()
start_room = "AA"
vaults_to_open = {vault for vault in rates if rates[vault] > 0}
minutes = 26

ways_to_open_vaults = generate_ways_to_open_vaults(start_room, vaults_to_open, [], minutes)
print(f"\tThere were only {len(ways_to_open_vaults)} considerable ways for the human to open vaults in {minutes} minutes.")
released_pressures = calculate_released_pressures(ways_to_open_vaults, minutes)
max_released_pressure = max(result[0] for result in released_pressures)
released_pressures.sort(key=lambda released_pressure: -released_pressure[0])
print(f"\tHe opened the vaults {released_pressures[0][1]}.")

# Now that we're two animals opening vaults, we want to find two routes that have no overlapping unopened vaults.
# To make it quicker, we sort the routes by best to worst. The human chooses route first.
# When the humans route route is worst than half of the current best score, we know that the best score must have been found.
max_released_pressure = 0
for human_route_index, (human_released_pressure, human_opened_vaults) in enumerate(released_pressures):
    if human_released_pressure >= (max_released_pressure / 2):
        for (elephant_released_pressure, elephant_opened_valuts) in released_pressures[human_route_index+1:]:
            if not (human_opened_vaults & elephant_opened_valuts):
                released_pressure = human_released_pressure + elephant_released_pressure
                if max_released_pressure < released_pressure:
                    max_released_pressure = released_pressure
                    human_best_opened_vaults = human_opened_vaults
                    elephant_best_opened_vaults = elephant_opened_valuts
print(f"\tSolved in {perf_counter() - start:0.1f}, answer: {max_released_pressure}")
print(f"\tThe human opened the following vaults: {human_best_opened_vaults}")
print(f"\tThe elephant opened the following vaults: {elephant_best_opened_vaults}")