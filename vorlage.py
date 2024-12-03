import time, re


def load(file):
    with open(file) as f:
        return [row.strip() for row in f]


def loesung(p):
    return p


time_start = time.perf_counter()
#print(f'Lösung Beispiel: {loesung(load("3/bsp1.txt"))}')
#print(f'Lösung: {loesung(load("3/p1.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')