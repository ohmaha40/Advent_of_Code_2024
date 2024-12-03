import time, re
#! https://adventofcode.com/2024/day/2


def load(file):
    with open(file) as f:
        return [row.strip() for row in f]

def solvep1(p):
    sicher = 0
    for row in p:
        code = []
        [code.append(int(i)) for i in re.findall("\d+", row)]
        if code[0] > code[1]:
            a = code[0]
            z = 1
            for i in code[1:]:
                if a > i and a <= (i+3):
                    a = i
                    z+=1
                else:
                    z=0
                    break
            if z == len(code):
                sicher += 1
        elif code[0] < code[1]:
            a = code[0]
            z = 1
            for i in code[1:]:
                if a < i and a >= (i-3):
                    a = i
                    z+=1
                else:
                    z=0
                    break
            if z == len(code):
                sicher += 1
    return sicher

        
def solvep2(p):
    sicher = 0
    for row in p:
        code = []
        [code.append(int(i)) for i in re.findall("\d+", row)]
        if code[0] >= code[1]:
            a = code[0]
            z = 1
            fehler = False
            for i in code[1:]:
                if code[0] == code[1]:
                    z +=1
                    fehler == True
                    continue
                if a > i and a <= (i+3):
                    a = i
                    z+=1
                elif fehler == False:
                    z += 1
                    fehler = True
                else:
                    break
            if z == len(code):
                sicher += 1
        elif code[0] <= code[1]:
            a = code[0]
            z = 1
            fehler = False
            for i in code[1:]:
                if code[0] == code[1]:
                    z +=1
                    fehler == True
                    continue
                if a == None or a < i and a >= (i-3):
                    a = i
                    z+=1
                elif fehler == False:
                    z += 1
                    fehler = True
                else:
                    break
            if z == len(code):
                sicher += 1
    return sicher

time_start = time.perf_counter()
#print(f'Part 1 Beispiel: {solvep1(load("2/bsp1.txt"))}')
print(f'Part 1: {solvep1(load("2/p1.txt"))}')
print(f'Part 2 Beispiel: {solvep2(load("2/bsp1.txt"))}')
print(f'Part 2: {solvep2(load("2/p1.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')