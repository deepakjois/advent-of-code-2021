import sys
from itertools import product

numbers = [int(n) for n in sys.stdin.readline().strip().split(",")]

grids = []
marks = []
while True:
    line = sys.stdin.readline()
    if not line:
        break

    g=[]
    m=[]
    for i in range(5):
        row = [int(n) for n in sys.stdin.readline().strip().split()]
        g.append(row)
        m.append([False]*5)

    grids.append(g)
    marks.append(m)

def mark(n):
    for (i, j, k) in product(range(len(grids)), range(5), range(5)):
            if grids[i][j][k] == n:
                marks[i][j][k] = True

def find_winner():
    for(i, j) in product(range(len(grids)), range(5)):
        if (all(m for m in marks[i][j]) or 
            all([marks[i][k][j] for k in range(5)])):
            return i

def find_score(winner, number):
    sum = 0
    for(i,j) in product(range(5), range(5)):
        sum = sum + (grids[winner][i][j] if not marks[winner][i][j] else 0)
    return sum * number

def parts():
    part = 1
    for n in numbers:
        mark(n)
        while (winner := find_winner()) is not None:
            if part == 1:
                print(find_score(winner, n))
                part = 2
            elif part == 2 and len(grids) == 1:
                print(find_score(winner, n))
                return
            del grids[winner]
            del marks[winner]

parts()