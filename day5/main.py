import logging
import math
import os
import sys
from time import perf_counter

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

def compute_target_number( source, rules ):

    target=source

    # Check if the source is in a range of the rules
    for rule in rules:
        if source >= rule[1] and source < (rule[1] + rule[2]):
            # I am in the correct range
            target = source + ( rule[0] - rule[1])

    return target

def solve( file ):

    part1 = 0
    part2 = 1

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

    
    part1=1e12

    total_of_seeds=0
    for seed_index in range(0,len(seeds),2):
        total_of_seeds += seeds[seed_index+1]
    print(f"Number of seeds : {total_of_seeds}")
    fraction_01=math.ceil(total_of_seeds/10000)
    t1_start = perf_counter()

    # All the maps are done, compute way
    index=0
    for seed_index in range(0,len(seeds),2):
        for seed in range(seeds[seed_index],seeds[seed_index]+seeds[seed_index+1]):
            index += 1
            if (index % fraction_01) == 1:
                t1_stop = perf_counter()
                print(f"Reach over {total_of_seeds} reached {index*100/total_of_seeds:.2f}% (elapsed(s): {t1_stop-t1_start:.4f}), index {index}.")
            source_category="seed"
            source_number=seed
            seeds_dict={}
#            print(f"{source_category} {source_number}, ", end="")
            while True:
                # Select the map
                try:
                    target_category=targets[source_category]
                except:
                    break
                map=source_category+"-to-"+target_category

                target_number=compute_target_number(source_number, maps[map]['rules'])

#                print(f"{target_category} {target_number}, ", end="")
                seeds_dict[target_category]=target_number

                # Prepare next target
                source_number=target_number
                source_category=target_category
#            print('')
            if seeds_dict["location"] < part1:
                part1=seeds_dict["location"]

                print(f"Location is {part1}")

    return part1, part2

def main() -> int:
    # --- Day 5: If You Give A Seed A Fertilizer ---
    # https://adventofcode.com/2023/day/5
    t1_start = perf_counter()
    value_part1, value_part2 = solve( "inputs/personnal.input" )
    t1_stop = perf_counter()
    print(f"Day 5: part 1 is {value_part1} and part 2 is {value_part2}.")
    print(f"Elapsed time(s): {t1_stop-t1_start}")
    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
