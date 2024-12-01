import time, re


def load(file):
    with open(file) as f:
        return re.findall("\d+", f.read())

def solvep1(p):
    left = sorted([int(p[i]) for i in range(0,len(p),2)])
    right = sorted([int(p[i]) for i in range(1,len(p),2)])
    part1 = sum(abs(b-a) for a,b in zip(left,right))
    part2 = sum(a*right.count(a) for a,b in zip(left,right))
    return part1, part2
    

def solvep2(p):
    return p

time_start = time.perf_counter()
#print(f'Part 1 Beispiel: {solvep1(load("1/bsp_p1.txt"))}')
print(f'Part 1: {solvep1(load("1/input.txt"))}')
#print(f'Part 2 Beispiel: {solvep2(load("1/bsp_p2.txt"))}')
#print(f'Part 2: {solvep2(load("1/input.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')