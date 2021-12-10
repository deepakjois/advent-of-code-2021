import sys
import queue
from itertools import product
from functools import reduce

grid = [[int(c) for c in line.strip()] for line in sys.stdin]

def neighbors(x,y):
    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for (dx, dy) in dirs:
         if x + dx >= 0 and (x + dx) < len(grid) and (y + dy) >= 0 and (y + dy) < len(grid[0]):
             yield (x+dx, y+dy)

def basin_size(x,y):
    q = queue.Queue()
    v = set()
    q.put((x,y))
    v.add((x,y))
    size = 1
    while not q.empty():
        x, y = q.get()
        val = grid[x][y]
        for nx, ny in neighbors(x,y):
            if (nx, ny) in v:
                continue
            adj = grid[nx][ny]
            if adj > val and adj < 9:
                size = size + 1
                q.put((nx, ny))
                v.add((nx, ny))
    return size

risk_level = 0
basins = []
for (x,y) in product(range(len(grid)), range(len(grid[0]))):
    val = grid[x][y]
    min = True
    for (nx, ny) in neighbors(x,y):
        adj = grid[nx][ny]
        if val >= adj:
            min = False
            break
    if min:
        risk_level = risk_level + val + 1
        basins.append(basin_size(x,y))

print(risk_level)
basins.sort(reverse=True)
print(reduce(lambda r, x: r * x, basins[0:3], 1))