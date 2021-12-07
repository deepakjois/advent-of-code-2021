import sys
from functools import reduce

crabs = list(map(lambda x: int(x), sys.stdin.readline().split(",")))
crabs.sort()
low, high = crabs[0], crabs[-1]

def print_min_cost(cost_fn):
    cost = [reduce(lambda cost, x: cost + cost_fn(abs(x-i)), crabs, 0) for i in range(low, high+1)]
    print(min(cost))

def part1():
    print_min_cost(lambda x: x)    

def part2():
    print_min_cost(lambda x: x * (x + 1) // 2)

part1()
part2()