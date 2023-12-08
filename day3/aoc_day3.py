import logging
import os
import sys
import pandas as pd

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

def aoc_day3( file ):

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, file)

    data = pd.read_csv(filename, header=None)
    df = data[0].apply(lambda x: pd.Series(list(x)))

    symbols_dict={}

    number=""
    is_part_number = False
    part_list=[]
    gear_dict={}
    current_gears={}

    for y in range(len(df.columns)):
        for x in range(len(df)):
            if not df[x][y].isnumeric() and not df[x][y] == ".":
                symbols_dict[df[x][y]] = True

    for y in range(len(df)):
        for x in range(len(df.columns)):
            if df[x][y].isnumeric():
                number = number + df[x][y]
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        try:
                            if df[x+i][y+j] in symbols_dict:
                                is_part_number = True
                                if df[x+i][y+j] == "*":
                                    # This is a gear
                                    key=str(x+i) + "-" + str(y+j)
                                    if key not in current_gears:
                                        current_gears[key] = True
                                continue
                        except KeyError:
                            continue
                try:
                    next_character = df[x+1][y]
                except KeyError:
                    next_character = "."
                if not next_character.isnumeric():
                    # We reach the end of a number
                    if number and is_part_number:
                        part_list.append(number)
                        for key in current_gears:
                            if key not in gear_dict:
                                gear_dict[key] = []
                            gear_dict[key].append(number)
                        
                    number=""
                    current_gears={}
                    is_part_number=False
    part1 = 0
    part_list_wo_dup = list(dict.fromkeys(part_list))
    for value in part_list:
        # Duplicate parts are removed
        part1 = part1 + int(value)
    part2 = 0
    for gear in gear_dict:
        list_of_parts = gear_dict[gear]
        if len(list_of_parts) == 2:
            # This is a correct gear
            part2= part2 + int(list_of_parts[0])*int(list_of_parts[1])

    return part1, part2



def main() -> int:
    # --- Day 3: Gear Ratios ---
    value_part1, value_part2 = aoc_day3( "inputs/day3.input" )

    logging.info(f"Day 3: part 1 is {value_part1} and part 2 is {value_part2}.")

    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
