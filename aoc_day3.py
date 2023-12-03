import logging
import sys
import pandas as pd

def aoc_day3( file ):

    data = pd.read_csv(file, header=None)
    df = data[0].apply(lambda x: pd.Series(list(x)))

    symbols="*#+$/=%&"
    symbols_dict={}
    number=""
    is_part_number = False
    part_list=[]

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
                    number=""
                    is_part_number=False
    part1 = 0
    part_list_wo_dup = list(dict.fromkeys(part_list))
    for value in part_list:
        # Duplicate parts are removed
        part1 = part1 + int(value)
    part2 = 0

    return part1, part2

def main() -> int:
    # --- Day 3: Gear Ratios ---
    value_part1, value_part2 = aoc_day3("inputs/day3.input")
    print(f"Day 3: part 1 is {value_part1} and part 2 is {value_part2}.")

    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
