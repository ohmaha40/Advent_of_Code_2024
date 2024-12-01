
#! inspiriert HexTree YouTube

import time, re
from collections import Counter

list1, list2 = [], []
def load(file):
    with open(file) as f:
        for row in f.readlines():
            x,y = (int(i) for i in row.split())
            list1.append(x), list2.append(y)
        list2.sort()
        list1.sort()


def solvep1(p):
    return sum(abs(list1[i]-list2[i])for i in range(len(list1)))
        #? schöne Lösung! durch Sort einfach For Schleife

def solvep2(p):
    c = Counter(list2)
    return sum(list1[i]*c[list1[i]] for i in range(len(list2)))

time_start = time.perf_counter()
#print(f'Part 1 Beispiel: {solvep1(load("1/bsp_p1.txt"))}')
print(f'Part 1: {solvep1(load("1/input.txt"))}')
#print(f'Part 2 Beispiel: {solvep2(load("1/bsp_p2.txt"))}')
print(f'Part 2: {solvep2(load("1/input.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')