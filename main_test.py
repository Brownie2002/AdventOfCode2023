from main import aoc_day1, aoc_day2

def test_aoc_day1():
    part1, part2 = aoc_day1("inputs/day1_test_part1.input")
    assert part1 == 142
    assert part2 == 142
    part1, part2 = aoc_day1("inputs/day1_test_part2.input")
    assert part1 == 209
    assert part2 == 281
    # My data
    part1, part2 = aoc_day1("inputs/day1.input")
    assert part1 == 54634
    assert part2 == 53855 

def test_aoc_day2():
    total, power = aoc_day2("inputs/day2_test.input")
    assert total == 8
    assert power == 2286
    # My data
    total, power = aoc_day2("inputs/day2.input")
    assert total == 1853
    assert power == 72706