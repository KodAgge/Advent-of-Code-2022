from common import load_file

def find_optimal_max_amount_geodes(
    ore_robot_ore, 
    clay_robot_ore, 
    obsidian_robot_ore, obsidian_robot_clay, 
    geode_robot_ore, geode_robot_obsidian, 
    T
):
    # We're doing a depth first search to be able to skip as many already seen states as possible

    # The state is:
    # (ore, clay, obsidian, geode, ore_robots, clay_robots, obsidian_robots, geode_robots, time_left)
    state = (0, 0, 0, 0, 1, 0, 0, 0, T)
    queue = [state]
    max_geode = 0
    most_expensive_ore_recipe = max([ore_robot_ore, clay_robot_ore, obsidian_robot_ore, geode_robot_ore])
    seen_states = set()

    while queue:
        state = queue.pop()
        ore, clay, obsidian, geode, ore_robots, clay_robots, obsidian_robots, geode_robots, time = state

        max_geode = max(max_geode, geode)
        if time == 0:
            continue

        # To speed up the calculation, we want to reduce the state space, which would make it more likely to skip a state.
        # First, we can cap the number of non-geode robots since only one robot can be produced at a time,
        # and after a while, it will only be worth to produce geode robots.
        # Second, we can cap the amount of ore, clay, and obsidian since there is only a maximum amount of it that
        # can be used productively until the time is up.

        # No need to build more ore robots than the most exepnsive ore recipe, since robots are built one at a time
        ore_robots = min(ore_robots, most_expensive_ore_recipe)

        # No need to build more clay robots when there is as many as the cost for the obsidian robot
        clay_robots = min(clay_robots, obsidian_robot_clay)
        
        # No need to build more obsidian robots when there is as many as the cost for the geode robot
        obsidian_robots = min(obsidian_robots, geode_robot_obsidian)

        # No need to keep track of more ore than can be spent during the remaining time,
        # which is the most expensive ore recipe times the time left.
        # Since we will also earn ore during the remaining time, we can subtract the 
        # amount of ore we will earn until the last turn.
        ore = min(ore, time * most_expensive_ore_recipe - (time - 1) * ore_robots)

        # No need to keep track of more clay than can be spent during the remaining time,
        # which is the clay cost for the obsidian recipe.
        # Since we will also earn clay during the remaining time, we can subtract the 
        # amount of clay we will earn until the last turn.
        clay = min(clay, time * obsidian_robot_clay - (time - 1) * clay_robots)

        # No need to keep track of more obsidian than can be spent during the remaining time,
        # which is the obsidian cost for the geode recipe.
        # Since we will also earn obsidian during the remaining time, we can subtract the 
        # amount of obsidian we will earn until the last turn.
        obsidian = min(obsidian,  time * geode_robot_obsidian - (time - 1) * obsidian_robots)

        state = (ore, clay, obsidian, geode, ore_robots, clay_robots, obsidian_robots, geode_robots, time)

        if state in seen_states:
            continue

        seen_states.add(state)

        # Do nothing
        queue.append(
                (ore + ore_robots, 
                clay + clay_robots, 
                obsidian + obsidian_robots, 
                geode + geode_robots, 
                ore_robots, 
                clay_robots, 
                obsidian_robots, 
                geode_robots, 
                time - 1)
            )

        # Build an ore robot
        if ore >= ore_robot_ore:
            queue.append(
                (ore + ore_robots - ore_robot_ore, 
                clay + clay_robots, 
                obsidian + obsidian_robots, 
                geode + geode_robots, 
                ore_robots + 1, 
                clay_robots, 
                obsidian_robots, 
                geode_robots, 
                time - 1)
            )

        # Build a clay robot
        if ore >= clay_robot_ore:
            queue.append(
                (ore + ore_robots - clay_robot_ore, 
                clay + clay_robots, 
                obsidian + obsidian_robots, 
                geode + geode_robots, 
                ore_robots, 
                clay_robots + 1, 
                obsidian_robots, 
                geode_robots, 
                time - 1)
            )

        # Build an obisidan robot
        if ore >= obsidian_robot_ore and clay >= obsidian_robot_clay:
            queue.append(
                (ore + ore_robots - obsidian_robot_ore, 
                clay + clay_robots - obsidian_robot_clay, 
                obsidian + obsidian_robots, 
                geode + geode_robots, 
                ore_robots, 
                clay_robots, 
                obsidian_robots + 1, 
                geode_robots, 
                time - 1)
            )

        # Build a geode robot
        if ore >= geode_robot_ore and obsidian >= geode_robot_obsidian:
            queue.append(
                (ore + ore_robots - geode_robot_ore, 
                clay + clay_robots, 
                obsidian + obsidian_robots - geode_robot_obsidian, 
                geode + geode_robots, 
                ore_robots, 
                clay_robots, 
                obsidian_robots, 
                geode_robots + 1, 
                time - 1)
            )
    
    return max_geode

parsed_lines = [list(map(int,[l[6], l[12], l[18], l[21], l[27], l[30]])) for l in [line.strip().split() for line in load_file()]]

# Part 1
T = 24
quality_level_sum = 0
print("Part 1:")
for i, (ore_robot_ore, clay_robot_ore, obsidian_robot_ore, obsidian_robot_clay, geode_robot_ore, geode_robot_obsidian) in enumerate(parsed_lines):
    max_geode = find_optimal_max_amount_geodes(
                    ore_robot_ore, 
                    clay_robot_ore, 
                    obsidian_robot_ore, obsidian_robot_clay, 
                    geode_robot_ore, geode_robot_obsidian, 
                    T
                )
    print(".", end="")
    quality_level_sum += (i + 1) * max_geode
    
print(f"the sum of the quality levels was {quality_level_sum}")

# Part 2
T = 32
quality_produdct = 1
print("\nPart 2:")
for i, (ore_robot_ore, clay_robot_ore, obsidian_robot_ore, obsidian_robot_clay, geode_robot_ore, geode_robot_obsidian) in enumerate(parsed_lines[:3]):
    max_geode = find_optimal_max_amount_geodes(
                    ore_robot_ore, 
                    clay_robot_ore, 
                    obsidian_robot_ore, obsidian_robot_clay, 
                    geode_robot_ore, geode_robot_obsidian, 
                    T
                )
    print(".", end="")
    quality_produdct *= max_geode
    
print(f"the product of the quality levels was {quality_produdct}")