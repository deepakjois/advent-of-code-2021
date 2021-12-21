import sys

def die():
    i = 1
    while True:
        yield i
        i = i + 1
        if i > 100:
            i = 1

p1_pos = int(sys.stdin.readline().strip().split(":")[1])
p2_pos = int(sys.stdin.readline().strip().split(":")[1])
print(p1_pos, p2_pos)

p1 = { "pos": p1_pos, "score": 0}
p2 = { "pos": p2_pos, "score": 0}
turn = 0
players = [p1, p2]
count = 0
d = die()
while True:
    a, b, c = next(d), next(d), next(d)
    count = count + 3
    p = players[turn]
    new_pos = (p["pos"] - 1 + a + b + c) % 10 + 1
    p["score"] += new_pos
    p["pos"] = new_pos
    print(f"player {turn+1} rolls {(a,b,c)} and moves to space {new_pos} for a total score of {p['score']}")
    if p["score"] >= 1000:
        break
    turn = (turn + 1) % 2

loser = (turn + 1) % 2
print(players[loser]["score"] * count)

