import sys
import queue
from itertools import product, chain

grid = [[int(c) for c in line.strip()] for line in sys.stdin]

def neighbors(x,y):
    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1), (1,1), (1,-1), (-1,1), (-1,-1)]
    for (dx, dy) in dirs:
         if x + dx >= 0 and (x + dx) < len(grid) and (y + dy) >= 0 and (y + dy) < len(grid[0]):
             yield (x+dx, y+dy)

flashes = 0
step = 0
while(True):
    step = step + 1

    q = queue.Queue()
    for (i,j) in product(range(len(grid)), range(len(grid[0]))):
        grid[i][j] = grid[i][j] + 1
        if grid[i][j] > 9:
            q.put((i,j))

    f = 0
    v = set()
    while not q.empty():
        x,y = q.get()
        if (x,y) in v:
           continue
        for (i,j) in neighbors(x,y):
            if (i,j) in v:
                continue
            grid[i][j] = grid[i][j] + 1
            if grid[i][j] > 9:
                q.put((i,j))
        f = f + 1
        grid[x][y] = 0
        v.add((x,y))

    flashes = flashes + f
    if step == 100:
        print(flashes)

    if all(n == 0 for n in chain.from_iterable(grid)):
        break

print(step)