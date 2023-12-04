from aoc_day_template import aoc_day_template

def test_example():
    part1, part2 = aoc_day_template("inputs/day_template_test1.input")
    assert part1 == 0
    assert part2 == 1

def test_internet_examples():
    # From https://www.reddit.com/r/adventofcode/comments/189q9wv/2023_day_3_another_sample_grid_to_use/
    part1, part2 = aoc_day_template("inputs/day_template_test2.input")
    assert part1 == 0
    assert part2 == 1
    part1, part2 = aoc_day_template("inputs/day_template_test3.input")
    assert part1 == 0
    assert part2 == 1

def test_my_data():
    part1, part2 = aoc_day_template("inputs/day_template.input")
    assert part1 == 0
    assert part2 == 1