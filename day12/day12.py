import logging
import os
import sys
from time import perf_counter

import pandas as pd
import numpy as np

logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))

def initialize ( file ):

    dirname = os.path.dirname( __file__ )
    filename = os.path.join(dirname, file)

    reports=[]

    with open(filename) as f:
        for line in f:
            report, groups = line.strip().split()
            groups = [int(x) for x in groups.split(",")]
            reports.append({"report": report, "groups": groups})

    return reports

def count_arrangements_subgroup(nb_items, group_to_test):
    nb_sol = 0
    nb_spaces = len(group_to_test)
    if "#" not in group_to_test:
                # Only "?" in the group
        nb_sol = nb_spaces - nb_items + 1
    else:
                # There is some given positions
        first_item = group_to_test.find('#')
        last_item = group_to_test.rfind('#')
        nb_sol_left = min(first_item + 1, nb_items)
        nb_sol_right = min(len(group_to_test) - last_item, nb_items)

        nb_sol = min(nb_sol_left,nb_sol_right)
    logging.debug(f"The sub-group {group_to_test} has {nb_sol} possibilities.")
    return nb_sol

def place_a_group(report, groups):

    group_size = groups[0]
    group = report[0:group_size]
    if group_size > len(report):
        # Impossible, group bigger than report
        return -1, None
    
    if group_size < len(report) and report[group_size] == "#":
        # Impossible, group cannot be followed by "#"
        return -2, 0

    if len(groups) == 1:
        # This group is the last.
        # Test ending conditions
        if "#" in report[group_size:]:
            # Impossible, the last group has to catch remaining "#"
            return -3, 0
        else:
            # This last group is OK. We count the number of possibilities with this group
            nb = count_arrangements_subgroup(group_size, group)
            if nb <= 0:
                raise Exception("Nb. of arrangements should be a least 1...")
            return nb, None

    next_report = report[group_size + 1:]
    nb_arrangements = 0
    a_arrangements = {}
    a_arrangements[len(groups)]=[]
    while True:
        nb_arrangements, toto = place_a_group(next_report, groups[1:])
        if nb_arrangements < 0 and nb_arrangements != -4:
            # There is no more groups to test at this level
            if toto:
                a_arrangements.update(toto)
            # Current group level is completed
            nb_arrangements == -4
            return nb_arrangements, a_arrangements
        a_arrangements[len(groups)].append(nb_arrangements)      
        if next_report[0] != "#":
            # Testing the other positions 
            next_report = next_report[1:]

    # Need to stop and test all possible groups !!
    return index, group

def count_arrangements(report, groups):

    num_arrangements = 0

    report_tmp = report

    while True:
        # Place first group
        nb_arrangements, arrangements = place_a_group(report_tmp, groups)
        if nb_arrangements == -2:
            # This group is followed by "#", test next position 
            report_tmp=report_tmp[1:]
    

    obvious_groups = list(filter(None,report.split(".") ))
    nb_sol_groups = []

    # TODO : Need to find how to split the report and possible groups !

    # Split the report in possible groups
    if len(groups) == len(obvious_groups):
        # The number of groups identify is equal to number of groups declared
        for i in range(len(groups)):
            nb_items  = groups[i]
            group_to_test = obvious_groups[i]

            # Count the number of arrangements in the sub-group
            nb_sol = count_arrangements_subgroup(nb_items, group_to_test)

            nb_sol_groups.append(nb_sol)
        possibilities = 1
        for i in nb_sol_groups:
            possibilities *= nb_sol_groups[i]
        logging.debug(f"The report has {possibilities} possibilities.")

    return num_arrangements

def solve( file):
    solution={"part1": 0, "part2":0}

    reports = initialize( file )

    t1_start = perf_counter()  
    ### Start of usefull code

    total_arrangements=0
    for report in reports:
        arrangements = count_arrangements(report["report"], report["groups"])
        total_arrangements += arrangements

    solution["part1"] = total_arrangements

    ### Ending of usefull code
    t1_stop = perf_counter()
    logging.info(f"Elapse time for both parts is {t1_stop-t1_start:.3f}(s).")

    return solution["part1"], solution["part2"]

def main() -> int:
    # --- Day 12: Hot Springs ---

    t1_start = perf_counter()
    value_part1, value_part2 = solve( "inputs/test2.input")
    t1_stop = perf_counter()
    logging.info(f"Elapsed total time: {t1_stop-t1_start:.3f}(s)")
    print(f"Day 12: part 1 is [{value_part1}] and part 2 is [{value_part2}].")
    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
