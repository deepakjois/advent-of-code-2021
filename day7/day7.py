import sys
from itertools import product
from collections import defaultdict

crabs = list(map(lambda x: int(x), sys.stdin.readline().split(",")))

def part1():
    cost = [0] * len(crabs)
    for (i,j) in product(range(len(crabs)), range(len(crabs))):    
        cost[i] = cost[i] + abs(crabs[i] - crabs[j])
    print(min(cost))

def part2():
    crabs.sort()
    low = crabs[0]
    high = crabs[-1]
    cost = defaultdict(lambda:0)
    for (i,j) in product(range(low, high+1), range(len(crabs))):
        n = abs(crabs[j] - i)
        cost[i] = cost[i] + (n * (n+1))//2
    print(min(cost.values()))

part1()
part2()