import logging
import math
import os
import sys
from time import perf_counter
from collections import Counter, OrderedDict
import pandas as pd

from aoc_lib.aoc_math import euclide
import numpy as np
import re

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

def initialize ( file ):

    dirname = os.path.dirname( __file__ )
    filename = os.path.join(dirname, file)

    values=[]
    with open(filename, "r") as f:
        for line in f:
            if line.strip():
                values.append([ int(x) for x in line.split() ])
    return values

def compute_next_line(sequence):

    new_sequence=[]
    for i in range(1, len(sequence)):
        new_sequence.append(sequence[i] - sequence[i-1])

    if np.count_nonzero(new_sequence) != 0:
        # The sequence is not only zeros
        next_value = compute_next_line(new_sequence)
    next_value=sequence[-1] + new_sequence[-1]
    previous_value=sequence[0] - new_sequence[0]
    logging.debug(f"Next value is {next_value}.")
    sequence.append(next_value)
    sequence.insert(0,previous_value)

    return sequence

def solve( file ):
    solution={"part1": 0, "part2":-1}

    sequences = initialize( file )

    t1_start = perf_counter()  

    total=0
    total_part2=0
    i=0
    for sequence in sequences:
        i =+ 1
        sequence = compute_next_line(sequence)
        total += sequence[-1]
        total_part2 += sequence[0]

        logging.debug(f"Next for line {i} value is {sequence[-1]}.")
        logging.debug(f"Previous for line {i} value is {sequence[0]}.")


    logging.debug(f"Total part1 value is {total}.")
    logging.debug(f"Total part2 is {total_part2}.")

    solution["part1"]=total
    solution["part2"]=total_part2

    t1_stop = perf_counter()  
    logging.info(f"Elapse time for both parts is {t1_stop-t1_start:.3f}(s).")

    return solution["part1"], solution["part2"]

def main() -> int:
    # --- Day 9: Mirage Maintenance ---

    t1_start = perf_counter()
    value_part1, value_part2 = solve( "inputs/personnal.input" )
    t1_stop = perf_counter()
    logging.info(f"Elapsed total time: {t1_stop-t1_start:.3f}(s)")
    print(f"Day 8: part 1 is [{value_part1}] and part 2 is [{value_part2}].")
    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
