from main import solve

def test_example():
    part1, part2 = solve("inputs/test1.input")
    assert part1 == 35
    assert part2 == 46

def test_my_data():
    part1, part2 = solve("inputs/personnal.input")
    assert part1 == 178159714
    assert part2 == 1