import sys
from itertools import product
from heapq import heappop, heappush

grid_in = [[int(c) for c in line.strip()] for line in sys.stdin]
l_in = len(grid_in)

l = l_in * 5
grid = [[0]*l for _ in range(l)]

vals = [i for i in range(9)]
vals[0] = 9
for (i,j) in product(range(5), range(5)):
    for (x,y) in product(range(l_in), range(l_in)):
        v = vals[(grid_in[x][y] + i + j) % 9]
        nx, ny = x + i * l_in, y + j * l_in
        grid[nx][ny] = v

def neighbors(pos):
    x, y = pos
    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for (dx, dy) in dirs:
         if x + dx >= 0 and (x + dx) < l and (y + dy) >= 0 and (y + dy) < l:
             yield (x+dx, y+dy)

cost = [[sys.maxsize]*l for _ in range(l)]
cost[0][0] = 0
q = [(0, (0,0))]
while q:
    c,pos = heappop(q)
    for (nx,ny) in neighbors(pos):
        if cost[nx][ny] > c + grid[nx][ny]:
            cost[nx][ny] = c + grid[nx][ny]
            heappush(q, (cost[nx][ny], (nx,ny)))

print(cost[l-1][l-1])