import logging
import os
import sys
from time import perf_counter

import pandas as pd

from aoc_lib.aoc_graph import graph

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

class Point:

    directions=["NW","N","NE","W","None","E","SW","S","SE"]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = ""
        self.direction = ""
        self.origin = ""
        self.seen = False
    
    def eq_position(self, point):
        if point.x == self.x and point.y == self.y:
            return True
        return False

class Metadata:
    
    def __init__(self):
        self.value = ""
        self.direction = ""
        self.counter=0

def initialize ( file ):

    dirname = os.path.dirname( __file__ )
    filename = os.path.join(dirname, file)

    data = pd.read_csv(filename, header=None)
    maze = data[0].apply(lambda x: pd.Series(list(x)))

    return maze

def find_next_positions(point,df):
    x = point.x
    y = point.y

    # Initialise
    positions=[]
    # symbols to search
    symbols_dict={"|":0,"-":0,"L":0,"J":0,"7":0,"F":0,"S":0,".":0}

    # Search the possible positions
    # In DataFrame : df[column][row]
    # In Point : x = columns, y = row 
    tested_direction = -1
    for j in [-1,0,1]:
        for i in [-1,0,1]:
            tested_direction += 1
            try:
                column=x+i
                row=y+j
                value=df[column][row]
                if df[column][row] in symbols_dict:
                    # Find a solution
                    find_point=Point(column, row)

                    find_point.value=value
                    find_point.direction=Point.directions[tested_direction]
                    
                    positions.append(find_point)

                    continue
            except KeyError:
                continue
    
    return positions


def test_positions(point, incoming_value):
    # Test a targeted point
    # Return the possible path. In this maze
    # * only cardinals are possible (N,E,S,W)

    possible={}
    possible["N"]={
        "incoming_direction":["S","|","7","F"],
        "impossible_previous":["-","7","F"]
        }
    possible["E"]={
        "incoming_direction":["S","-","J","7"],
        "impossible_previous":["|","J","7"]
        }
    possible["S"]={
        "incoming_direction":["S","|","J","L"],
        "impossible_previous":["-","J","L"]
        }
    possible["W"]={
        "incoming_direction":["S","-","L","F"],
        "impossible_previous":["|","F","L"]
        }

    origin_to_tested = point.direction
    origin_value = incoming_value
    tested_value = point.value

    if origin_to_tested not in possible:
        # Point in not in cardinal position
        return False

    if tested_value not in possible[origin_to_tested]["incoming_direction"]:
        # Tested value is not compatible with incomming direction
        return False
    
    if origin_value in possible[origin_to_tested]["impossible_previous"]:
        # Point value is not compatible with previous position
        return False

    return True

def solve( file ):
    solution={"part1": 0, "part2":-1}

    maze = initialize( file )
    df_sol = pd.DataFrame().reindex_like(maze)
    t1_start = perf_counter()  

    ### Start of usefull code

    start_position = maze[maze.isin(["S"])].dropna(how='all').dropna(axis=1)

    start_point = Point(int(start_position.columns[0]), int(start_position.index[0]))
    start_point.value="S"
    previous_point = Point(-1,-1)

    df_sol[start_point.x][start_point.y]=Metadata()
    df_sol[start_point.x][start_point.y].value="S"

    loop=True
    counter=0
    while loop:
        counter += 1

        next_positions = find_next_positions(start_point,maze)

        # Test possible next possible positions
        for possibility in next_positions:
            is_possible = test_positions(possibility, start_point.value) and not possibility.eq_position(previous_point)
            is_possible = test_positions(possibility, start_point.value) and not possibility.eq_position(previous_point)
            if is_possible:
                # This point is the next available (possible and not seen)
                logging.debug(f"Next {possibility.value} at {possibility.x} , {possibility.y} ")
                if possibility.value != "S":
                    df_sol[possibility.x][possibility.y]=Metadata()
                    df_sol[possibility.x][possibility.y].value=possibility.value
                    df_sol[start_point.x][start_point.y].direction=possibility.direction
                df_sol[start_point.x][start_point.y].counter=counter
                previous_point=start_point
                start_point=possibility
                if start_point.value == "S":
                    # We reached the start, a loop is done
                    loop=False

                break
    
    number_in = 0

    df = pd.DataFrame().reindex_like(df_sol)
    df = df.fillna("Z")

    symbols_dict={"|":"║","-":"═","L":"╚","J":"╝","7":"╗","F":"╔","S":"*",".":" "}

    # Solution given by : https://www.reddit.com/r/adventofcode/comments/18eza5g
    for i in range(0,len(df_sol.index)):
        inside=False
        crossing_counter=0
        first_delta = ""
        for j in range(0,len(df.columns)):
            item=df_sol[j][i]

            if i == len(df_sol.index) -1 :
                item_below=df_sol[j][i]
            else:
                item_below=df_sol[j][i+1]

            if not pd.isna(item):
                #df[j][i] = symbols[item.direction]
                df[j][i] = symbols_dict[item.value]

            if not pd.isna(item) and not pd.isna(item_below):
                # If item and below ar in the path
                delta = item.counter - item_below.counter
                if delta in [-1,1]:
                    # if we enter for the first time
                    if inside is False:
                        inside = True
                        first_delta = delta
                    crossing_counter=crossing_counter + delta

            # Handle if the first cross is up or down ...
            if pd.isna(item):
                if ( first_delta and first_delta < 0) and crossing_counter < 0:
                    df[j][i]="☺"
                    number_in = number_in + 1
                elif ( first_delta and first_delta > 0) and crossing_counter > 0:
                    df[j][i]="☺"
                    number_in = number_in + 1                    

    solution["part1"] = int(counter/2)
    solution["part2"] = number_in

    ### Ending of usefull code
    t1_stop = perf_counter()
    logging.info(f"Elapse time for both parts is {t1_stop-t1_start:.3f}(s).")

    graph(df)

    return solution["part1"], solution["part2"]

def main() -> int:
    # --- Day 10: Pipe Maze ---

    t1_start = perf_counter()
    value_part1, value_part2 = solve( "inputs/test1.input" )
    t1_stop = perf_counter()
    logging.info(f"Elapsed total time: {t1_stop-t1_start:.3f}(s)")
    print(f"Day 10: part 1 is [{value_part1}] and part 2 is [{value_part2}].")
    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
