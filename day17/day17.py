import sys

def simulate(vx,vy, xl, xr, yt, yb):
    x,y = 0,0
    while y >= yb:
        x,y = x + vx, y + vy
        if x >= xl and x <= xr and y <= yt and y >= yb:
            return True

        dx = 0 if vx == 0 else -1 if vx > 0 else 1
        vx = vx + dx
        vy = vy - 1

    return False

xl,xr,yt,yb = 57, 116, -148, -198
count = 0
for vx in range(1,xr+1):
    for vy in range(yb,-yb):
        if simulate(vx,vy, xl, xr, yt, yb):
            count = count + 1

print(count)