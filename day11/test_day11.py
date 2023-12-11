from day11 import solve
from day11_brute import solve_brute_force

def test_example1_brute_10():
    part1, part2 = solve_brute_force("inputs/test1.input", 10)
    assert part1 == 374
    assert part2 == 1030

def test_example1_brute_100():
    part1, part2 = solve_brute_force("inputs/test1.input", 100)
    assert part1 == 374
    assert part2 == 8410

def test_example1_brute_1000():
    part1, part2 = solve_brute_force("inputs/test1.input", 1000)
    assert part1 == 374
    assert part2 == 82210


def test_example1_10():
    part1, part2 = solve("inputs/test1.input", 10)
    assert part1 == 374
    assert part2 == 1030

def test_example1_100():
    part1, part2 = solve("inputs/test1.input", 100)
    assert part1 == 374
    assert part2 == 8410

def test_example1_1000():
    part1, part2 = solve("inputs/test1.input", 1000)
    assert part1 == 374
    assert part2 == 82210

def test_my_data():
    # Leave default value of expansion
    part1, part2 = solve("inputs/personnal.input")
    assert part1 == 9556712
    assert part2 == 678626199476