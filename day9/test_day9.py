from day9 import solve

def test_example1():
    part1, part2 = solve("inputs/test1.input")
    assert part1 == 114
    assert part2 == 2


def test_my_data():
    part1, part2 = solve("inputs/personnal.input")
    assert part1 == 1798691765
    assert part2 == 1104