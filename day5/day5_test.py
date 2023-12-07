from day5 import solve2

def test_example():
    part1, part2 = solve2("inputs/test1.input")
    assert part1 == 35
    assert part2 == 46

def test_my_data():
    part1, part2 = solve2("inputs/personnal.input")
    assert part1 == 178159714
    assert part2 == 100165128