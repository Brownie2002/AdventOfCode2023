from day6 import solve

def test_example():
    part1, part2 = solve("inputs/test1.input")
    assert part1 == 288
    assert part2 == 71503

def test_my_data():
    part1, part2 = solve("inputs/personnal.input")
    assert part1 == 1195150
    assert part2 == 42550411