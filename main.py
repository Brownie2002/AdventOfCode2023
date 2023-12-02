import logging
import sys

def test_aoc_day1():
    assert aoc_day1("inputs/day1_test1.lst", "part2") == 281

def aoc_day1( file, i ) -> int:
    """Day 1: Trebuchet?!"""
    # Download the input locally from the AoC server
    # https://adventofcode.com/2023/day/1/input
    calibratrion_value=0

    digits_list={}
    digits_list["part1"]=["0", "1", "2", "3","4","5","6","7","8","9"]
    digits_list["part2"]=["aaaaaa", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "0", "1", "2", "3","4","5","6","7","8","9"]

    part="part2"

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
            logging.debug(f'The intermediate value is: {two_digits_value}' )
            calibratrion_value=calibratrion_value + int(two_digits_value)
    return calibratrion_value

def test_aoc_day2():
    total, power = aoc_day2("inputs/day2_test.input")
    assert total == 8
    assert power == 2286

def aoc_day2_possible(red, green, blue):
    nb_cubes_red=12
    nb_cubes_green=13
    nb_cubes_blue=14

    if red > nb_cubes_red or green > nb_cubes_green or blue > nb_cubes_blue:
        logging.debug('Too many cubes of one color.')
        return False

    return True

def aoc_day2( file ) -> int:

    total = 0
    power = 0

    with open(file) as f:
        for line in f:
            # Check each Game
            test = True
            subset_detail = {'red': 0, 'green': 0, 'blue': 0}
            min_value = {'red': 0, 'green': 0, 'blue': 0}
            game=line.rstrip('\n').split(":")
            game_value=int(game[0].split(" ")[1])
            for set in game[1].split(";"):
                for subset in set.strip().split(","):
                    color=subset.strip().split(" ")
                    subset_detail[color[1]]=int(color[0])
                    if int(color[0]) > min_value[color[1]]:
                        min_value[color[1]] = int(color[0])
                if test:
                    test = aoc_day2_possible(subset_detail['red'], subset_detail["green"], subset_detail["blue"])
            if test:                    
                logging.debug(f"Test {game_value} possible")
                total = total + game_value
            else:
                logging.debug(f"Test {game_value} impossible")
            power = power + min_value["red"]*min_value["green"]*min_value["blue"]

    logging.debug(f"The total value is {total}")
    logging.debug(f"The total power is {power}")
    return total, power


def main() -> int:
    logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

    # --- Day 1: Trebuchet?! ---
    calibration_value = aoc_day1('inputs/day1.input', "part2")
    print(f"Day 1: Calibration value is {calibration_value}.")

    # --- Day 2: Cube Conundrum ---
    sum_of_winning_games, power_of_sets = aoc_day2("inputs/day2.input")
    print(f"Day 2: Sum of games value is {sum_of_winning_games}.")
    print(f"Day 2: Power of sets {power_of_sets}.")

    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
