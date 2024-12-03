import time, re
#! https://adventofcode.com/2024/day/3
#! https://www.youtube.com/@Gravitar

def load(file):
    with open(file) as f:
        return f.read()


def loesung(p):
    part1 = part2 = 0
    status = True
    for do, dont, a, b in re.findall(r"(do\(\))|(don't\(\))|mul\((\d+),(\d+)\)", p):
        if do or dont:
            status = do
            continue
        e= int(a) * int(b)
        part1 += e
        if status:
            e = int(a) * int(b)
            part2 += e
    return part1, part2

time_start = time.perf_counter()
#print(f'Lösung Beispiel: {loesung(load("3/bsp2.txt"))}')
print(f'Lösung: {loesung(load("3/p1.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')