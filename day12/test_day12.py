from day12 import solve, count_arrangements

def test_arrangements():
    assert count_arrangements("???.###", [1,1,3]) == 1
    assert count_arrangements(".??..??...?##.", [1,1,3])  == 0
    assert count_arrangements("?#?#?#?#?#?#?#?", [1,3,1,6])     == 1
    assert count_arrangements("????.#...#...", [4,1,1])         == 1
    assert count_arrangements("????.######..#####.", [1,6,5])   == 1
    assert count_arrangements("?###????????", [3,2,1])          == 1

def test_example1():
    part1, part2 = solve("inputs/test1.input")
    assert part1 == 21
    assert part2 == -1

def test_my_data():
    # Leave default value of expansion
    part1, part2 = solve("inputs/personnal.input")
    assert part1 == -1
    assert part2 == -1