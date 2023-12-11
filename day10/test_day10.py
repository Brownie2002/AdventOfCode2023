from day10 import solve

def test_example1():
    part1, part2 = solve("inputs/test1.input")
    assert part1 == 4
    assert part2 == 2

def test_example2():
    part1, part2 = solve("inputs/test2.input")
    assert part1 == 8
    assert part2 == 0

def test_example3():
    part1, part2 = solve("inputs/test3.input")
    assert part1 == 80
    assert part2 == 10

def test_my_data():
    part1, part2 = solve("inputs/personnal.input")
    assert part1 == 6812
    assert part2 == 527