import logging
import os
import sys
from time import perf_counter

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

def void_indexes ( galaxy ):

    # Find empty columns
    refactored = galaxy.replace(".",0)
    empty_columns = refactored.select_dtypes('number').columns
    empty_rows    = np.where(refactored.map(np.isreal).all(1))[0]
   
    return empty_rows, empty_columns

def solve( file , expand_value_part2 = 1000000):
    solution={"part1": 0, "part2":0}

    galaxy = initialize( file )

    t1_start = perf_counter()  
    ### Start of usefull code

    for part in ["part1", "part2"]:
        expand_value = 1
        if part == "part2":
            # -1 since they are replaced ...
            expand_value = expand_value_part2 - 1
        
        empty_rows, empty_columns = void_indexes ( galaxy )

        # x = row, y = column
        x, y = np.where(galaxy == "#")

        galaxy_list = []
        nb_galaxy = len(x)
        for i in range(nb_galaxy):
            x_origin = x[i]
            y_origin = y[i]

            nb_previous_x_expansion = len(np.where(empty_rows    < x_origin)[0])
            nb_previous_y_expansion = len(np.where(empty_columns < y_origin)[0])

            x_expanded = nb_previous_x_expansion * expand_value
            y_expanded = nb_previous_y_expansion * expand_value

            galaxy_list.append(Point(x[i] + x_expanded, y[i] + y_expanded))

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
    value_part1, value_part2 = solve( "inputs/test1.input", 100 )
    t1_stop = perf_counter()
    logging.info(f"Elapsed total time: {t1_stop-t1_start:.3f}(s)")
    print(f"Day 11: part 1 is [{value_part1}] and part 2 is [{value_part2}].")
    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
