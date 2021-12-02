import sys
import functools

commands = [(c[0], int(c[1])) for c in [s.split() for s in sys.stdin.readlines()]]


def part1(commands):
    pilot = {
        "up":      lambda c,i: (c[0], c[1]-i),
        "down":    lambda c,i: (c[0], c[1]+i),
        "forward": lambda c,i: (c[0]+i, c[1]),
    }

    course = functools.reduce(
        lambda course, command: pilot[command[0]](course, command[1]),
        commands,
        (0,0))

    print(course[0]*course[1])


def part2(commands):
    pilot = {
        "up":      lambda c,a,i: (c, a-i),
        "down":    lambda c,a,i: (c, a+i),
        "forward": lambda c,a,i: ((c[0]+i, c[1] + a*i), a),
    }

    course, aim = functools.reduce(
        lambda course_and_aim, command: pilot[command[0]](course_and_aim[0], course_and_aim[1], command[1]), 
        commands, 
        ((0,0), 0))

    print(course[0]*course[1])


part1(commands)
part2(commands)