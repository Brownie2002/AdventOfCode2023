
from aoc_day1 import aoc_day1

def test_example_part1():
    part1, part2 = aoc_day1("inputs/day1_test_part1.input")
    assert part1 == 142
    assert part2 == 142

def test_my_data():
    part1, part2 = aoc_day1("inputs/day1.input")
    assert part1 == 54634
    assert part2 == 53855 
