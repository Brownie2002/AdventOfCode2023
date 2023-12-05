import logging
import math
import os
import sys
from time import perf_counter

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

def initialize ( file ):

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, file)

    seeds=[]
    maps={}

    targets={}

    with open(filename, "r") as f:
        for line in f:
            if "seeds:" in line:
                seeds=[int(x) for x in line.split()[1:]]
                continue
            if " map:" in line:
                map=line.split()[0]
                current_map=map
                maps[current_map]={}
                maps[current_map]['rules']=[]
                source, target= map.split("-to-")
                targets[source]=target
                continue
            if not line.rstrip():
                # Skip blank line
                continue
            
            # We are on a line with numbers "dst_start, src_start, nb"
            maps[current_map]['rules'].append([int(x) for x in line.split()])

    return seeds, maps, targets

def compute_target_number( source_number, source_range, source_category, maps ):

    target_number=source_number
    remaining_range=1

    target_category=""

    for key in maps:
        source, target=key.split("-to-")
        if source == source_category:
            break
    
    rule_found=False
    next_range=1e12
    # Check if the source is in a range of the rules
    for rule in maps[source_category + "-to-" + target]["rules"]:
        if rule[0] - target_number and rule[0] > target_number: next_range=target_number + rule[0]
        if (source_number >= rule[1]) and (source_number < (rule[1] + rule[2])):
            # I am in the correct range
            rule_found=True
            target_number = source_number - rule[1] + rule[0]
            remaining_range = rule[0] + rule[2] - target_number
            if remaining_range > source_range:
                remaining_range=source_range
            break

    if not rule_found:
        logging.debug(f"No rule is found. No translation on part of the range")
        if next_range == 1e12:
            remaining_range=source_range
        else:
            remaining_range=next_range-target_number
    
    # Stop condition for recursion
    if target != 'location':
        target_number, remaining_range = compute_target_number(target_number,remaining_range,target, maps)
    return target_number, remaining_range

def solve2( file ):
    t0_start = perf_counter()

    part1=1e12
    part2=1e12
    solution={"part1": 1e12, "part2":1e12}

    seeds, maps, targets = initialize(file)

    total_of_seeds=0
    for seed_index in range(0,len(seeds),2):
        total_of_seeds += seeds[seed_index+1]
    print(f"Number of seeds : {total_of_seeds}")

    # All the maps are done, compute way

    seed_range={}
    t0_stop = perf_counter()

    for part in ["part1", "part2"]:
        t1_start = perf_counter()  
        increment=1
        if part == "part2":increment=2
        for seed_index in range(0,len(seeds),increment):
            source_number=seeds[seed_index]
            source_range=1
            if part == "part2":source_range=seeds[seed_index+1]
            seed_range[source_number]=source_range

        while seed_range:
            logging.debug(f"Seed ranges number: {len(seed_range)}")
            source_category="seed"

            source_number=next(iter(seed_range))
            source_range=seed_range.pop(source_number)

            target_number, target_range= compute_target_number( source_number, source_range, source_category, maps )
            
            if solution[part] > target_number:
                solution[part]=target_number

            logging.debug(f"Target number is {target_number} and is range is {target_range}")
            if source_range > target_range:
                seed_range[source_number+target_range]=source_range-target_range
        t1_stop = perf_counter()
        logging.info(f"Elapsed time {part}(s): {(t1_stop-t1_start) + (t0_stop-t0_start)}")
    return solution["part1"], solution["part2"]

def main() -> int:
    # --- Day 5: If You Give A Seed A Fertilizer ---
    # https://adventofcode.com/2023/day/5
    # See: https://github.com/morgoth1145/advent-of-code/blob/9344c2e30130f4d555e7b7393b65a52646bae00f/2023/05/solution.py
    t1_start = perf_counter()
    value_part1, value_part2 = solve2( "inputs/personnal.input" )
    t1_stop = perf_counter()
    print(f"Day 5: part 1 is {value_part1} and part 2 is {value_part2}.")
    print(f"Elapsed total time(s): {t1_stop-t1_start}")
    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
