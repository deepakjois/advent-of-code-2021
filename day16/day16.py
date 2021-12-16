import sys
from itertools import chain
from operator import mul
from functools import reduce

stream = [bin(int(c, 16))[2:].rjust(4, '0') for c in sys.stdin.readline().strip()] 
stream = list(chain.from_iterable(stream))

pos = 0
total_version = 0

def parse_packet():
    global stream, pos, total_version

    version = int("".join(stream[pos:pos+3]), 2)
    total_version = total_version + version
    pos = pos + 3

    type = int("".join(stream[pos:pos+3]), 2)
    pos = pos + 3

    if type == 4:
        num_str = ""
        while True:
            num = stream[pos:pos+5]
            num_str = num_str + "".join(num[1:])
            pos = pos + 5
            if num[0] == '0':
                break
        number = int(num_str, 2)
        return number
    else :
        literals = []
        if stream[pos] == '0':
            l = int("".join(stream[pos+1:pos+16]), 2)
            pos = pos + 16
            end = pos + l
            while pos < end:
                literals.append(parse_packet())
        else:
            c = int("".join(stream[pos+1:pos+12]), 2)
            pos = pos + 12
            for i in range(c):
                literals.append(parse_packet())

        return eval(type, literals)

def eval(op, vals):
    if op == 0:
        return sum(vals)
    elif op == 1:
        return reduce(mul, vals, 1)
    elif op == 2:
        return min(vals)
    elif op == 3:
        return max(vals)
    elif op == 5:
        return 1 if vals[0] > vals[1] else 0
    elif op == 6:
        return 1 if vals[0] < vals[1] else 0
    elif op == 7:
        return 1 if vals[0] == vals[1] else 0

val = parse_packet()
print(total_version)
print(val)