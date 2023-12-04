import os
import sys
import pandas as pd

def aoc_day_template( file ):

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, file)

    print(f"Input full path: {filename}")

    data = pd.read_csv(filename, header=None, sep=r"\s+|:")
    print(data)
    index=-1
    for col in data.values[:1][0]:
        index+=1
        if col == "|":
            break
    print(f"The separator is at position {index}")

    for index, row in data.iterrows():
        print(row)
        for item in row.values:
            print(item)
        print("tets")

    print(col)
    # Find card separation column
    separator=data[:][0].columns.get_loc("|")

    part1 = 0
    part2 = 1

    return part1, part2

def main() -> int:
    # --- Day 4: Scratchcards ---
    value_part1, value_part2 = aoc_day_template( "inputs/day4_test1.input" )
    print(f"Day 4: part 1 is {value_part1} and part 2 is {value_part2}.")

    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
