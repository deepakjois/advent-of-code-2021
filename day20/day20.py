import sys

def get_square(p):
    x, y = p
    return [
        (x-1,y-1), (x, y-1), (x+1, y-1),
        (x-1, y), (x,y), (x+1, y),
        (x-1, y+1), (x, y+1), (x+1, y+1)
    ]

enhance = [('1' if c == '#' else '0') for c in sys.stdin.readline().strip()]
# print(enhance)
print(len(enhance))

sys.stdin.readline()

points = set()
for y, line in enumerate(sys.stdin.readlines()):
    line = line.strip()
    for x, c in enumerate(line):
        if c == "#":
            points.add((x,y))

print(f"{len(points)} added")
xmin = min(x for x,_ in points)
xmax = max(x for x,_ in points)
ymin = min(y for _,y in points)
ymax = max(y for _,y in points)
default_value = '0'
# print(sorted(points))
for i in range(50):
    pnew = set()
    tl = (xmin,ymin)
    br = (xmax,ymax)
    def get_on_value(p):
        x, y = p
        if x > xmax or x < xmin or y > ymax or y < ymin:
            return default_value
        return '1' if p in points else '0'

    # print(tl, br)
    for x in range(tl[0]-1, br[0]+2):
        for y in range(tl[1]-1, br[1]+2):
            sq = get_square((x,y))
            n = "".join([get_on_value(p) for p in sq])
            # print(n)
            n = int(n, 2)
            # print(n)
            if enhance[n] == '1':
                pnew.add((x,y))
    points = pnew
    xmin -= 1
    xmax += 1
    ymin -= 1
    ymax += 1
    default_value = '0' if default_value == '1' else '1'

print(len(points))