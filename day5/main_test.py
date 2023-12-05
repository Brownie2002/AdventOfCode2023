from main import solve

def test_example():
    part1, part2 = solve("inputs/test1.input")
    assert part1 == 35
    assert part2 == 1

def test_my_data():
    part1, part2 = solve("inputs/personnal.input")
    assert part1 == 0
    assert part2 == 1