import sys
from collections import defaultdict

graph = defaultdict(lambda: set())
for line in sys.stdin:
    n = line.strip().split('-')
    graph[n[0]].add(n[1])
    graph[n[1]].add(n[0])

def paths(curr, can_visit_cave, visited = defaultdict(lambda: 0)):
    if curr  ==  "end":
        return 1
    visited[curr] = visited[curr] + 1
    path_count = 0
    for next in graph[curr]:
        if next == "start":
            continue
        if can_visit_cave(next, visited):
            path_count = path_count + paths(next, can_visit_cave, visited)
    visited[curr] = visited[curr] - 1
    return path_count

print(paths("start", lambda n,v: n.isupper() or v[n] == 0))
print(paths("start", lambda n,v: n.isupper() or not (v[n] > 0 and any(c.islower() and v[c] == 2 for c in v))))