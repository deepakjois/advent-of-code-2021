import sys

points = set()
for line in sys.stdin:
    line = line.strip()
    if len(line) == 0:
        break
    line = line.split(",")
    x, y = int(line[0]), int(line[1])
    points.add((x,y))

for line in sys.stdin:
    fold = line.lstrip("fold along ").split("=")
    dir, last = fold[0], int(fold[1])
    if dir == 'x':
        lastx = last
        reflect_if_beyond_fold = lambda p: (2 * lastx - p[0] , p[1]) if p[0] > lastx else p
    else:
        lasty = last
        reflect_if_beyond_fold = lambda p: (p[0], 2 * lasty - p[1]) if p[1] > lasty else p
    
    for p in list(points):
        points.add(reflect_if_beyond_fold(p))

for y in range(lasty):
    s = ['#' if (x,y) in points else '.' for x in range(lastx)]
    print("".join(s))
