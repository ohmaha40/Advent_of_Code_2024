import time, re


def load(file):
    with open(file) as f:
        return [row.strip().split() for row in f] 


def solvep1(p):
    liste1, liste2 = [] , []
    part1 = 0
    for zahl in p:
        liste1.append(zahl[0])
        liste2.append(zahl[1])
    for i in range(0, len(liste1)):
        k1 = int(min(liste1))
        k2 = int(min(liste2))
        liste1.pop(liste1.index(min(liste1)))
        liste2.pop(liste2.index(min(liste2)))
        if k1 >= k2:
            part1 += k1-k2
        else:
            part1 += k2-k1
    return part1

def solvep2(p):
    liste1, liste2 = [] , []
    part2 = 0
    for zahl1 in p:
        liste1.append(zahl1[0])
        liste2.append(zahl1[1])
    for i in liste1:
        z=0
        for a in liste2:
            if int(a) == int(i):
                z += 1
        part2 += (int(i)*z)
    return part2

time_start = time.perf_counter()
print(f'Part 1 Beispiel: {solvep1(load("1/bsp_p1.txt"))}')
print(f'Part 1: {solvep1(load("1/input.txt"))}')
#print(f'Part 2 Beispiel: {solvep2(load("1/bsp_p2.txt"))}')
#print(f'Part 2: {solvep2(load("1/input.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')