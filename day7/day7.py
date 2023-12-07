import logging
import math
import os
import sys
from time import perf_counter
from collections import Counter, OrderedDict
import pandas as pd

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

# To let you count characters while preserving order of first appearance
class OrderedCounter(Counter, OrderedDict): pass

# Dict to assign a score to a repetition of cards
_score = {5:60, 4: 50, 3:30, 2: 10, 1:0}
# 60 : Five of a kind, where all five cards have the same label: AAAAA
# 50 : Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# 40 (30 + 10) :Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# 30 : Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# 20 (10+10) : Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# 10 :One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# 0  : High card, where all cards' labels are distinct: 23456

def find_duplicate(word):
    return [(ch, cnt) for ch, cnt in OrderedCounter(word).items() if cnt >= 1]

def initialize ( file ):

    dirname = os.path.dirname( __file__ )
    filename = os.path.join(dirname, file)

    times=[]
    distances=[]

    with open(filename, "r") as f:
        hands=[]
        bids=[]
        for line in f:
            hand, bid = line.split()
            hands.append(hand)
            bids.append(int(bid))

    return hands, bids

def compute_hand_value(hand, part):

    # For part2, Jockers have to be added to the biggest value
    # Jocker have to be added to a a Three of a Kind than a pair
    hand_value=0
    values = OrderedCounter(hand)
    if "J" in values and part == "part2":
        # Handle the Joker
        num_J=values["J"]
        if num_J != 5:
            del values["J"]
            # Update the better hand
            key_better_hand=max(values.items(), key=lambda x: x[1])[0]
            values[key_better_hand] = values[key_better_hand] + num_J
    for key in values:
        hand_value = hand_value + _score[values[key]]

    return hand_value

def solve( file ):
    solution={"part1": 1, "part2":0}

    hands, bids = initialize( file )

    for part in ["part1", "part2"]:
        t1_start = perf_counter()  

        df = pd.DataFrame({'Hands': hands, 'Bids': bids})

        # Compute strengh of hands
        df['Strengh']=df['Hands'].apply(lambda x: compute_hand_value(x, part))
        df2 = df['Hands'].str.split('', expand=True)
        df = pd.concat([df,df2], axis=1)

        # Use categoric series
        for i in range(1,6):
            if part == "part1":
                df[i] = pd.Categorical(df[i], ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"])
            else:
                df[i] = pd.Categorical(df[i], ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"])

        df = df.sort_values(['Strengh', 1,2,3,4,5], ascending=[False,True,True,True,True,True])
        df.insert(0, 'Rank', range(len(df), 0,-1))

        solution[part] = (df['Rank']*df['Bids']).sum()
        t1_stop = perf_counter()  
        logging.info(f"Elapse time for {part} is {t1_stop-t1_start:.3f}(s).")
    return solution["part1"], solution["part2"]

def main() -> int:
    # --- Day 7: Camel Cards ---

    t1_start = perf_counter()
    value_part1, value_part2 = solve( "inputs/personnal.input" )
    t1_stop = perf_counter()
    logging.info(f"Elapsed total time(s): {t1_stop-t1_start}")
    print(f"Day 7: part 1 is [{value_part1}] and part 2 is [{value_part2}].")
    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
