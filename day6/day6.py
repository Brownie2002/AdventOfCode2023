import logging
import math
import os
import sys
from time import perf_counter

import pandas as pd

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

def initialize ( file ):

    dirname = os.path.dirname( __file__ )
    filename = os.path.join(dirname, file)

    times=[]
    distances=[]

    with open(filename, "r") as f:

        for line in f:
            if "Time:" in line:
                times=[int(x) for x in line.split()[1:]]
                continue
            if "Distance:" in line:
                distances=[int(x) for x in line.split()[1:]]
                continue
    return times, distances

def compute_distances(time, distance):

    df = pd.DataFrame()
    df.insert(0, 'speed/hold', range(0, time))
    df.insert(0, 'time', time)
    df['travel_time']=df["time"] - df["speed/hold"]
    df['travel_distance']=df["speed/hold"]*df['travel_time']

    number_of_ways_to_win = df['travel_distance'].gt(distance).sum()

    return number_of_ways_to_win

def solve( file ):
    solution={"part1": 1, "part2":0}

    times, distances = initialize( file )

    result=1
    for i in range(len(times)):
        solution["part1"] = solution["part1"] * compute_distances(times[i], distances[i])

    times_kerning=int(''.join(str(x) for x in times))
    distances_kerning=int(''.join(str(x) for x in distances))
    solution["part2"] = compute_distances(times_kerning,distances_kerning)

    return solution["part1"], solution["part2"]

def main() -> int:
    # --- Day 6: Wait For It ---

    t1_start = perf_counter()
    value_part1, value_part2 = solve( "inputs/personnal.input" )
    t1_stop = perf_counter()
    print(f"Day 6: part 1 is {value_part1} and part 2 is {value_part2}.")
    print(f"Elapsed total time(s): {t1_stop-t1_start}")
    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
