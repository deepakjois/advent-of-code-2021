from functools import cache
from itertools import product

@cache
def play(state=((5, 0), (10, 0), 0)):
    all_wins = (0, 0)
    for (a,b,c) in product(range(1,4), range(1,4), range(1,4)):
        sum = a + b + c
        turn = state[2]
        pos, score = state[turn]
        new_pos = (pos - 1 + sum) % 10 + 1
        new_score = score + new_pos
        if new_score >= 21:
            if turn == 0:
                all_wins = (all_wins[0]+1, all_wins[1])
            else:
                all_wins = (all_wins[0], all_wins[1]+1)
        else:
            p1, p2, turn = state
            if turn == 0:
                updated = ((new_pos,new_score), p2, 1)
            else:
                updated = (p1, (new_pos,new_score), 0)

            wins = play(updated) 
            all_wins = (all_wins[0]+wins[0], all_wins[1]+wins[1])

    return all_wins

print(max(play()))