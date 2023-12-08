import logging
import os
import sys
import numpy as np

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

def aoc_day4( file ):

    part1 = 0
    part2 = 1

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, file)

    score=0

    logging.info(f"Input full path: {filename}")

    num_original_cards=0
    with open(filename, "rb") as f:
        num_original_cards = sum(1 for _ in f)

    nb_cards=np.full(num_original_cards, 1)

    with open(filename) as f:
        for line in f:
            nb_match = 0
            info=line.rstrip('\n').split(":")
            card_number=int(info[0].split()[1])
            winning, having=info[1].strip().split("|")
            having=having.split()
            for win_number in winning.split():
                if win_number in having:
                    nb_match += 1
            for new_card in range(nb_match):
                logging.debug(f"with card {card_number} win card {new_card + card_number + 1}")
                nb_cards[new_card + card_number] +=  nb_cards[card_number - 1]
            if nb_match > 0:
                score = score + 2**(nb_match-1)

    part1=score
    part2=np.sum(nb_cards)  
    # Find card separation column

    return part1, part2

def main() -> int:
    # --- Day 4: Scratchcards ---
    value_part1, value_part2 = aoc_day4( "inputs/day4.input" )
    print(f"Day 4: part 1 is {value_part1} and part 2 is {value_part2}.")

    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
