import sys
from collections import Counter
from itertools import tee
from operator import sub

start = sys.stdin.readline().strip()
freq = Counter(start)

pairs = ("".join(t) for t in zip(start, start[1:]))
pair_freq = Counter(pairs)

sys.stdin.readline()

rules = dict(l.strip().split(" -> ") for l in sys.stdin.readlines())

for _ in range(40):
    new_pair_freq = Counter()
    for pair, count in pair_freq.items():
        if pair in rules:
            c = rules[pair]
            p1, p2 = pair[0] + c, c + pair[1]

            freq.update({c: count})
            new_pair_freq.update({p1: count, p2: count})

    pair_freq = new_pair_freq

diff = sub(*[f(x) for f, x in zip([max, min], tee(freq.values()))])
print(diff)