import time, itertools as itt
#! https://adventofcode.com/2024/day/2


def load(file):
    with open(file) as f:
        return [list(map(int, row.split())) for row in f]

def check(report):
    diffs = {a-b for a,b in itt.pairwise(report)}
    return diffs.issubset({1,2,3}) or diffs.issubset({-1,-2,-3})

def solvep1(p)-> bool:
    part1 = part2 = 0
    for report in p:
        part1 += check(report)
        part2 += any(check(report[:i] + report[i+1:]) for i in range(len(report)))
    return part1 ,part2

time_start = time.perf_counter()
#print(f'Part 1 Beispiel: {solvep1(load("2/bsp1.txt"))}')
print(f'Part 1: {solvep1(load("2/p1.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')