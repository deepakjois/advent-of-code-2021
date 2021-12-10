import sys
from functools import reduce

match = { ')': '(', ']': '[', '}': '{', '>': '<' }
open = list(match.values())
match = {**match, **{v:k for k,v in match.items()}}

points_illegal = { ')': 3, ']': 57, '}': 1197, '>': 25137}
points_autocomplete = { ')': 1, ']': 2, '}': 3, '>': 4  }

lines = [[c for c in line.strip()] for line in sys.stdin]

score_illegal = 0
score_autocomplete = []

for line in lines:
    stack = []
    for c in line:
        if c in open:
            stack.append(c)
            continue
        m = match[c]
        if len(stack) == 0 or stack.pop() != m:
            score_illegal = score_illegal + points_illegal[c]
            stack = []
            break
    if len(stack) > 0:
        score = reduce(lambda score, c: score * 5 + points_autocomplete[match[c]], stack[::-1], 0)
        score_autocomplete.append(score)

print(score_illegal)
score_autocomplete.sort()
print(score_autocomplete[len(score_autocomplete)//2])
