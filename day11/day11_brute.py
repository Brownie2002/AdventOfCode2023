import logging
import os
import sys
from time import perf_counter
import warnings

import pandas as pd
import numpy as np

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def eq_position(self, point):
        if point.x == self.x and point.y == self.y:
            return True
        return False
    
    def distance(self, point):
        return abs(point.x - self.x) + abs(point.y - self.y)

def initialize ( file ):

    dirname = os.path.dirname( __file__ )
    filename = os.path.join(dirname, file)

    data = pd.read_csv(filename, header=None)
    galaxy = data[0].apply(lambda x: pd.Series(list(x)))

    return galaxy

def expand ( galaxy, expand_value ):
    warnings.warn("Brute force is time consuming !", ResourceWarning)
    # Used for brute force ... Not enough efficient

    # If expansion is 2,   we add  1 line/column
    # If expansion is 100, we add 99 line/column
    expand_value = expand_value - 1
    factor = 1 / (expand_value * 10)

    # Find empty columns
    refactored = galaxy.replace(".",0)
    empty_columns = refactored.select_dtypes('number').columns
    empty_rows    = np.where(refactored.map(np.isreal).all(1))[0]

    # Duplicate empty lines
    for i in empty_rows:
        increment = 0
        for j in range(expand_value):
            increment += factor
            refactored.loc[i+increment]=refactored.loc[i]
    refactored = refactored.sort_index().reset_index(drop=True)

    for i in empty_columns:
        increment = 0
        # Compute a list of index (float) to insert
        columns_id = [i + x/(expand_value+1) for x in range(1,expand_value+1)]
        df_to_concact = pd.DataFrame(0, index=np.arange(len(refactored.index)), columns=columns_id)
        refactored = pd.concat([refactored, df_to_concact], axis=1)

    refactored = refactored[sorted(refactored.columns)]
    refactored = refactored.set_axis(list(range(len(refactored.columns))), axis='columns')
   
    return refactored

def solve_brute_force( file, expand_value_part2 = 1000000 ):
    solution={"part1": 0, "part2":0}

    galaxy = initialize( file )

    t1_start = perf_counter()  
    ### Start of usefull code

    for part in ["part1", "part2"]:
        expand_value = 2
        if part == "part2":
            expand_value = expand_value_part2
        
        galaxy_expanded = expand( galaxy, expand_value )
        
        # x = row, y = column
        x, y = np.where(galaxy_expanded == "#")

        galaxy_list = []
        nb_galaxy = len(x)
        for i in range(nb_galaxy):
            galaxy_list.append(Point(x[i], y[i]))

        # pairs = n*(n-1)/2
        nb_pairs = int(nb_galaxy * (nb_galaxy - 1) /2)
        logging.info(f"Galaxy has {nb_pairs} pairs.")

        distance = 0
        count = 0
        for i in range(0,nb_galaxy):
            for j in range(i+1, nb_galaxy):
                count += 1
                distance += galaxy_list[i].distance(galaxy_list[j])

        solution[part] = distance

    ### Ending of usefull code
    t1_stop = perf_counter()
    logging.info(f"Elapse time for both parts is {t1_stop-t1_start:.3f}(s).")

    return solution["part1"], solution["part2"]

def main() -> int:
    # --- Day 11: Cosmic Expansion ---

    t1_start = perf_counter()
    value_part1, value_part2 = solve_brute_force( "inputs/test1.input", 100 )
    t1_stop = perf_counter()
    logging.info(f"Elapsed total time: {t1_stop-t1_start:.3f}(s)")
    print(f"Day 11 (Brute): part 1 is [{value_part1}] and part 2 is [{value_part2}].")
    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
