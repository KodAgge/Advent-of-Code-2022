from common import load_file
from time import perf_counter

read_lines = load_file(test=False)

parsed_lines = [[[int(sx[2:-1]), int(sy[2:-1])], [int(bx[2:-1]), int(by[2:])]] for _, _, sx, sy, _, _, _, _, bx, by in [line.strip().split() for line in read_lines]]

distances = []
beacon_indices = []
sensor_indices = []

for ((sx, sy), (bx, by)) in parsed_lines:
    distances.append(abs(sx-bx)+abs(sy-by))
    sensor_indices.append((sx,sy))
    beacon_indices.append((bx, by))

# ===== Part 1 version 1 =====
# This implementation was very slow and I had to rethink it several times for part 2
start = perf_counter()
y = 2000000
beacons_at_y = set(bx for (bx, by) in beacon_indices if by==y)
sensors_at_y = set(sx for (sx, sy) in sensor_indices if sy==y)
beacons_and_sensors_at_y = beacons_at_y.union(sensors_at_y)
imposible_beacon_indices = set()

for ((sx, sy), reach_distance) in zip(sensor_indices, distances):
    # If beacon can reach the chosen y-value
    if abs(y-sy) <= reach_distance:
        abs_distance = abs(y-sy)
        # Find the x-values it reaches at that row
        reachable_indices = [x+sx for x in range(abs_distance-reach_distance, reach_distance-abs_distance+1)]
        for index in reachable_indices:
            if index not in beacons_and_sensors_at_y:
                # Add it to the impossible locations if it isn't a sensor or a beacon
                imposible_beacon_indices.add(index)

print(f"Answer part 1 version 1: {len(imposible_beacon_indices)}")
print(f"\tIt took {perf_counter()-start:0.2f} seconds to find.")


# ===== Part 1 version 2 =====
start = perf_counter()
y = 2000_000
intervals = []
beacons_at_y = set()

for ((sx, sy), (bx, by), sensor_reach_distance) in zip(sensor_indices, beacon_indices, distances):
    # Store the the intervals of the spots every beacon reaches on row y
    if (reach_distance_at_y := sensor_reach_distance - abs(y - sy)) >= 0:
        min_reach_x = sx - reach_distance_at_y
        max_reach_x = sx + reach_distance_at_y
        intervals.append((min_reach_x, max_reach_x))
        if by == y:
            beacons_at_y.add(bx)

# Sort the intervals so they go from lowest to highest starting x-value
intervals.sort()
interval_queue = [list(intervals[0])]

# Loop through intervals to merge overlapping ones
for x_start, x_end in intervals[1:]:
    queue_x_start, queue_x_end = interval_queue[-1]
    # If there is no overlap, add the interval
    if x_start > queue_x_end + 1:
        interval_queue.append([x_start, x_end])
    # If there is overlap, update the end to the end of the interval with the highest end
    else:
        interval_queue[-1][1] = max(queue_x_end, x_end)

impossible_indices = set()
for x_start, x_end in interval_queue:
    for x in range(x_start, x_end + 1):
        impossible_indices.add(x)
print(f"Answer part 1 version 2: {len(impossible_indices-beacons_at_y)}")
print(f"\tIt took {perf_counter()-start:0.2f} seconds to find.")


# ===== Part 2 =====
start = perf_counter()
Y_MAX = 4_000_000
X_MAX = 4_000_000
found_beacon = False
# Looping through the search grid by row to find beacon sending distress signal
for y in range(Y_MAX + 1):
    intervals = []

    for ((sx, sy), sensor_reach_distance) in zip(sensor_indices, distances):
        # Store the the intervals of the spots every beacon reaches on row y
        if (reach_distance_at_y := sensor_reach_distance - abs(y - sy)) >= 0:
            min_reach_x = sx - reach_distance_at_y
            max_reach_x = sx + reach_distance_at_y
            intervals.append((min_reach_x, max_reach_x))

    # Sort the intervals so they go from lowest to highest starting x-value
    intervals.sort()
    interval_queue = [list(intervals[0])]

    # Loop through intervals to merge overlapping ones
    for x_start, x_end in intervals[1:]:
        queue_x_start, queue_x_end = interval_queue[-1]
        # If there is no overlap, add the interval
        if x_start > queue_x_end + 1:
            interval_queue.append([x_start, x_end])
        # If there is overlap, update the end to the end of the interval with the highest end
        else:
            interval_queue[-1][1] = max(queue_x_end, x_end)

    # Checking if there is an x-value between 0 and X_MAX which is not in an interval
    x = 0
    for x_start, x_end in interval_queue:
        # If the current earliest possibly unreachable x-value, not yet covered by an interval,
        # is smaller than the start of the next interval, it will not be covered at all
        if x < x_start:
            print(f"Answer part 2: {4_000_000* x + y}")
            print(f"\tFound beacon at {(x, y)} with the tuning frequency {4_000_000* x + y}.")
            print(f"\tIt took {perf_counter()-start:0.2f} seconds to find.")
            found_beacon = True
            break

        # If it isn't smaller than the start, update it to the end of the interval if it is larger than it
        x = max(x, x_end + 1)

        # If the current earliest possibly unreachable x-value is outside the search grid, 
        # the beacon is not at this row
        if x > X_MAX:
            break

    if found_beacon:
        break