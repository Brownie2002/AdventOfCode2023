from aoc_day3 import aoc_day3

def test_example():
    part1, part2 = aoc_day3("inputs/day3_test1.input")
    assert part1 == 4361
    assert part2 == 467835

def test_internet_examples():
    # From https://www.reddit.com/r/adventofcode/comments/189q9wv/2023_day_3_another_sample_grid_to_use/
    part1, part2 = aoc_day3("inputs/day3_test2.input")
    assert part1 == 925
    assert part2 == 6756
    part1, part2 = aoc_day3("inputs/day3_test3.input")
    assert part1 == 413
    assert part2 == 6756

def test_my_data():
    part1, part2 = aoc_day3("inputs/day3.input")
    assert part1 == 550064
    assert part2 == 85010461