from day8 import solve

def test_example1():
    part1, part2 = solve("inputs/test1.input")
    assert part1 == 2
    assert part2 == 2

def test_example2():
    part1, part2 = solve("inputs/test2.input")
    assert part1 == 6
    assert part2 == 6

def test_my_data():
    part1, part2 = solve("inputs/personnal.input")
    assert part1 == 21409
    assert part2 == 21165830176709