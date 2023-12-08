from day7 import solve

def test_example():
    part1, part2 = solve("inputs/test1.input")
    assert part1 == 6440
    assert part2 == 5905

def test_my_data():
    part1, part2 = solve("inputs/personnal.input")
    assert part1 == 248105065
    assert part2 == 249515436