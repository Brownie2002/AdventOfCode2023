import logging
import sys

def aoc_day1( file ) -> int:
    """Day 1: Trebuchet?!"""
    # Download the input locally from the AoC server
    # https://adventofcode.com/2023/day/1/input
    calibratrion_value=0
    value = {}

    digits_list={}
    digits_list["part1"]=["0", "1", "2", "3","4","5","6","7","8","9"]
    digits_list["part2"]=["aaaaaa", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "0", "1", "2", "3","4","5","6","7","8","9"]

    part="part2"
    for part in "part1", "part2":
        calibratrion_value=0
        with open(file) as f:
            for line in f:
                first_index=99999
                last_index=-1
                first_value=""
                last_value=""
                for digit in digits_list[part]:
                    index1=line.find(digit)
                    index2=line.rfind(digit)
                    if index1 < first_index and index1 > -1:
                        first_value=digit
                        if len(digit) > 1:
                            first_value=str(digits_list[part].index(digit))
                        first_index=index1
                    if index2 > last_index:
                        last_value=digit
                        if len(digit) > 1:
                            last_value=str(digits_list[part].index(digit))
                        last_index=index2
                logging.debug(f"Values are {first_value} and {last_value}")
                
                two_digits_value=first_value+last_value
                logging.debug(f'The intermediate value is: **{two_digits_value}**' )
                try:
                    calibratrion_value=calibratrion_value + int(two_digits_value)
                except ValueError:
                    logging.error(f"Failure w/ value >{two_digits_value}< from {line}")
        value[part]=calibratrion_value

    return value["part1"], value["part2"]

def main() -> int:
    logging.basicConfig(encoding='utf-8', level=logging.INFO)

    # --- Day 1: Trebuchet?! ---
    calibration_value, calibration_value_updated = aoc_day1('inputs/day1.input')
    print(f"Day 1: Calibration value is {calibration_value} then {calibration_value_updated}.")

    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
