from day4 import aoc_day4

def test_example():
    part1, part2 = aoc_day4("inputs/day4_test1.input")
    assert part1 == 13
    assert part2 == 30

def test_my_data():
    part1, part2 = aoc_day4("inputs/day4.input")
    assert part1 == 21558
    assert part2 == 10425665