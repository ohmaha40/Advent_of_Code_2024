import time, re
#! https://adventofcode.com/2024/day/3

def load(file):
    with open(file) as f:
        return f.read()


def loesung(p):
    part1 = part2 = 0
    suchstring = r"mul\((\d+),(\d+)\)"
    part1 = sum([int(a)*int(b) for a,b in re.findall(suchstring, p)])
    suchstring_do = r"(do\(\)|don't\(\))"
    status = True
    for match in re.finditer(f"{suchstring_do}|{suchstring}" , p):
        content = match.group(0)
        if content == "do()":
            status = True
        elif content == "don't()":
            status = False
        elif status and re.match(suchstring, content):
            mul_match = re.match(suchstring, content)
            a, b =  map(int, mul_match.groups())
            part2 += (a * b)
    return part1, part2

time_start = time.perf_counter()
#print(f'Lösung Beispiel: {loesung(load("3/bsp2.txt"))}')
print(f'Lösung: {loesung(load("3/p1.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')