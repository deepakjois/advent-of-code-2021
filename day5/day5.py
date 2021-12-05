import sys
from itertools import product, chain, filterfalse, count
from functools import reduce

lines = []
for line in sys.stdin:
    line = line.strip()
    coords = map(lambda x: (int(x[0]), int(x[1])), map(lambda x: x.split(","), line.split(" -> ")))
    lines.append(list(coords))

mx, my = reduce(lambda m, l: (max(l[0][0], l[1][0], m[0]), max(l[0][1], l[1][1] ,m[1])), lines, (0,0))
map = [[0]*(my+1) for i in range(mx+1)]

sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)

def find_overlap_count(part):
    for [(x1,y1), (x2,y2)] in lines:
        dir = (sign(x2-x1), sign(y2-y1))
        if part == 1 and (dir[0] !=0 and dir[1] !=0):
            continue
        x, y = x1, y1
        while True:
            map[x][y] = map[x][y] + 1
            if (x,y) == (x2,y2):
                break
            x, y = x + dir[0], y + dir[1]

    count = len(list(filterfalse(lambda x: x <= 1, chain.from_iterable(map))))
    print(count)

find_overlap_count(1)
map = [[0]*(my+1) for i in range(mx+1)]
find_overlap_count(2)