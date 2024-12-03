import time, re


def load(file):
    with open(file) as f:
        return [row.strip() for row in f]


def solvep1(p):
    test =[1,2,3,4,5,6]
    for i in test[1:]:
        print(i)
    return p

def solvep2(p):
    return p

time_start = time.perf_counter()
solvep1(12)
#print(f'Part 1 Beispiel: {solvep1(load("1/bsp_p1.txt"))}')
#print(f'Part 1: {solvep1(load("1/input.txt"))}')
#print(f'Part 2 Beispiel: {solvep2(load("1/bsp_p2.txt"))}')
#print(f'Part 2: {solvep2(load("1/input.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')