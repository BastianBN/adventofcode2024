import re
import math

input_str = (
    """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
)


def part1():
    total = 0
    groups = re.findall("mul\((\d[0-9]*),(\d[0-9]*)\)", input_str)
    for group in groups:
        nbs_list = [int(x) for x in group]
        total += math.prod(nbs_list)
    print(total)


def part2():
    total = 0
    groups = re.finditer("mul\((\d[0-9]*),(\d[0-9]*)\)", input_str)
    dos = re.finditer("do\(\)", input_str)
    donts = re.finditer("don't\(\)", input_str)
    for group in groups:
        print(group)
    for do in dos:
        last_do = do.end()
        print(last_do)
    for dont in donts:
        last_dont = do.end()
        print(dont)


part1()
part2()
