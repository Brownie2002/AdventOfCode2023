import logging
import math
import os
import sys
from time import perf_counter
from collections import Counter, OrderedDict
import pandas as pd


import re

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

def initialize ( file ):

    dirname = os.path.dirname( __file__ )
    filename = os.path.join(dirname, file)

    maps={}
    instructions=""
    with open(filename, "r") as f:
        for line in f:
            if line.strip():
                if "=" in line:
                    position, left, right = re.sub("[,=()]","",line).split()
                    maps[position] = {"L": left, "R": right}
                else:
                    instructions=line.strip()

    return maps, instructions

def euclide(a, b):
    if b == 0: return a
    return euclide(b, a % b)

def compute_next_position(positions, maps, instructions):
    # Cannot do recursion, too many
    current_positions=positions
    current_index=maps[positions[0]]["index"]

    direction=(current_index) % len(instructions) # L or R
    next_positions=[]
    for item in positions:
        next_position=maps[item][instructions[direction]]
        next_positions.append(next_position)
        maps[next_position]["index"] = current_index + 1

    return next_positions

def find_positions(maps, letter):
    positions=[]
    for item in maps:
        if item[-1] == letter:
            positions.append(item)
    return positions

def solve( file ):
    solution={"part1": 0, "part2":-1}

    maps, instructions = initialize( file )

    for part in ["part1", "part2"]:
        t1_start = perf_counter()  

        if part == "part1":
            positions=["AAA"]
        else:
            positions=find_positions(maps, "A")
            nb_start_position = len(positions)
            
        for position in positions:
            maps[position]["index"] = 0

        found_end = False
        loops=[]
        while  not found_end:
            next_positions = compute_next_position(positions, maps, instructions)
            positions=next_positions
            if part == "part1" and positions[0] == "ZZZ":
                found_end=True
                solution[part] = maps['ZZZ']['index']
            if part == "part2":
                results=find_positions(next_positions, "Z")
                if len(results) > 0:
                    # An ending has been found
                    for result in results:
                        if result not in loops:
                            loops.append(maps[result]['index'])
                
                if len(loops) == nb_start_position:
                    # All loops are detected
                    found_end=True

                    # Solutions are looping. We need to find when the loops finish all together.
                    # nb_loop_A * size_loop_A = nb_loop_B * size_loop_B = PPCM(size_loop_A, size_loop_A)
                    # PPCM = Plus Petit Multiple Commun (See https://w.wiki/8RG9)
                    # PPCM can be computed from PGCD and Euclide algorithme
                    PPCM=loops[0]
                    for item in range(1,len(loops)):
                        PGCD=euclide(PPCM,loops[item])
                        PPCM=PPCM*loops[item]/PGCD

                    solution[part] = int(PPCM)


        
        t1_stop = perf_counter()  
        logging.info(f"Elapse time for {part} is {t1_stop-t1_start:.3f}(s).")
    return solution["part1"], solution["part2"]

def main() -> int:
    # --- Day 8: Haunted Wasteland ---

    t1_start = perf_counter()
    value_part1, value_part2 = solve( "inputs/personnal.input" )
    t1_stop = perf_counter()
    logging.info(f"Elapsed total time(s): {t1_stop-t1_start}")
    print(f"Day 8: part 1 is [{value_part1}] and part 2 is [{value_part2}].")
    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
