

from aoc_day2 import aoc_day2

def test_example():
    total, power = aoc_day2("inputs/day2_test.input")
    assert total == 8
    assert power == 2286
def test_my_data():
    # My data
    total, power = aoc_day2("inputs/day2.input")
    assert total == 1853
    assert power == 72706