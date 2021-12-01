import sys

report = [int(depth) for depth in sys.stdin.readlines()]

def part1(report):
    count = sum(a > b for (a,b) in zip(report[1:],report))
    print(count)

def part2(report):
    windows = list(zip(report, report[1:], report[2:]))
    count = sum(sum(a) > sum(b) for (a,b) in zip(windows[1:], windows))
    print(count)

part1(report.copy())
part2(report.copy())