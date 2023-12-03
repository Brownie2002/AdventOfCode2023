import logging
import sys

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
    # --- Day 2: Cube Conundrum ---
    sum_of_winning_games, power_of_sets = aoc_day2("inputs/day2.input")
    print(f"Day 2: Sum of games value is {sum_of_winning_games} and power if {power_of_sets}.")

    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
