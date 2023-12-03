import logging
import sys

from aoc_day1 import aoc_day1
from aoc_day2 import aoc_day2

def main() -> int:
    logging.basicConfig(encoding='utf-8', level=logging.INFO)

    # --- Day 1: Trebuchet?! ---
    calibration_value, calibration_value_updated = aoc_day1('inputs/day1.input')
    print(f"Day 1: Calibration value is {calibration_value} then {calibration_value_updated}.")

    # --- Day 2: Cube Conundrum ---
    sum_of_winning_games, power_of_sets = aoc_day2("inputs/day2.input")
    print(f"Day 2: Sum of games value is {sum_of_winning_games} and power if {power_of_sets}.")

    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
