import os
import sys
import pandas as pd

def aoc_day_template( file ):

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, file)

    print(f"Input full path: {filename}")

    part1 = 0
    part2 = 1

    return part1, part2

def main() -> int:
    # --- Day template ---
    value_part1, value_part2 = aoc_day_template( "inputs/day_template.input" )
    print(f"Day template: part 1 is {value_part1} and part 2 is {value_part2}.")

    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
