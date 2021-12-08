import sys

sum = 0
for line in sys.stdin:
    line =  line.split("|")
    inputs = ["".join(sorted(i)) for i in line[0].split()]
    outputs = ["".join(sorted(i)) for i in line[1].split()]
    map = {}

    def find(l,fn):
        return next(x for x in l if fn(x))

    map['1'] = find(inputs, lambda x: len(x) == 2)
    map['4'] = find(inputs, lambda x: len(x) == 4)
    map['7'] = find(inputs, lambda x: len(x) == 3)
    map['8'] = find(inputs, lambda x: len(x) == 7)

    zero_six_nine = [x for x in inputs if len(x) == 6]
    map['6'] = find(zero_six_nine, lambda x: not set(map['7']).issubset(set(x)))
    map['9'] = find(zero_six_nine, lambda x: set(map['4']).issubset(set(x)))
    map['0'] = find(zero_six_nine, lambda x: x != map['6'] and x != map['9'])

    two_three_five = [x for x in inputs if len(x) == 5]
    map['3'] = find(two_three_five, lambda x: set(map['7']).issubset(set(x)))
    map['5'] = find(two_three_five, lambda x: x != map['3'] and set(x).issubset(set(map['9'])))
    map['2'] = find(two_three_five, lambda x: x != map['3'] and x != map['5'])

    map = {v: k for k, v in map.items()}
    num = int("".join([map[k] for k in outputs]))
    sum = sum + num

print(sum)

