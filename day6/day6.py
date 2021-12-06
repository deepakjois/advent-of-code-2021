import sys

fishes = list(map(lambda x: int(x), sys.stdin.readline().split(",")))

liveness_count = {x:0 for x in range(9)}
for num_days_left in fishes:
    liveness_count[num_days_left] = liveness_count[num_days_left] + 1

curr_day = 0
while (curr_day < 256):
    for i in range(9):
        if liveness_count[i] > 0:
            days_skip = i + 1
            break

    delta = {x:0 for x in range(9)}
    delta[days_skip-1] = -liveness_count[days_skip-1]
    delta[6] = liveness_count[days_skip-1]
    delta[8] = liveness_count[days_skip-1]
    for i in range(days_skip, 9):
        if liveness_count[i] > 0:
            delta[i] = delta[i]-liveness_count[i]
            delta[i-days_skip] = delta[i-days_skip]+liveness_count[i]

    for i in range(9):
        liveness_count[i] = liveness_count[i] + delta[i]
    
    curr_day = curr_day + days_skip

sum = sum([liveness_count[k] for k in liveness_count])
print(sum)

