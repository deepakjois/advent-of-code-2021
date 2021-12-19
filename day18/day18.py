import sys
from itertools import product

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def treeify(pair):
    if pair.count("[") == 0:
        return Node(int(pair)) 

    pair = pair[1:len(pair)-1]
    if pair.count("[") == 0:
        n = Node(",")
        l, r = pair.split(",")
        n.left = Node(int(l))
        n.right = Node(int(r))
        return n
    
    match = 0
    p = 0
    while True:
        if pair[p] == "[":
            match = match + 1
        elif pair[p] == "]":
            match = match - 1
        elif pair[p] == ",":
            if match == 0:
                break
        p = p + 1

    n = Node(",")
    n.left = treeify(pair[:p])
    n.right = treeify(pair[p+1:])
    return n

def untreeify(t):
    if t.left is None and t.right is None:
      return str(t.val)

    if t.val == ",":
        return "[" + untreeify(t.left) + "," + untreeify(t.right) + "]"

def inorder(n, arr=[]):
    if n == None:
        return arr
    inorder(n.left,arr)
    # print(f"appending {n.val}")
    arr.append(n)
    inorder(n.right, arr)
    return arr

def find_explode_node(t,l=0):
    if t is None:
        return None
    if t.left and isinstance(t.left.val, int) and t.right and isinstance(t.right.val, int) and l >= 4:
        return t

    le = find_explode_node(t.left, l+1)
    re = find_explode_node(t.right, l+1)

    return le if le else re

def explode(pair):
    t = treeify(pair)
    en = find_explode_node(t)
    if en is None:
        return pair
    l, r = en.left.val, en.right.val
    # print(l, r)
    en.val = 0
    en.left = None
    en.right = None
    io = inorder(t, [])
    # print(list(map(lambda x: x.val, io)))
    for idx, n in enumerate(io):
        if n == en:
               lefts = list(x for x in io[:idx] if isinstance(x.val, int))
               if len(lefts) > 0:
                   lefts[-1].val = lefts[-1].val + l
               rights = list(x for x in io[idx+1:] if isinstance(x.val, int))
               if len(rights) > 0:
                   rights[0].val = rights[0].val + r
               # print(lefts)
               # print(rights)
    return untreeify(t)

def find_split_node(t):
    if t is None:
        return None 

    if isinstance(t.val, int) and t.val >= 10:
        return t
    
    l = find_split_node(t.left)
    r = find_split_node(t.right)
    return l if l else r

def split(pair):
    t = treeify(pair)
    sn = find_split_node(t)
    if sn is None:
        return pair
    
    v = sn.val
    sn.val = ","
    sn.left = Node(v//2)
    sn.right = Node(v//2 + v%2)
    return untreeify(t)

def reduce(pair):
    while True:
        # print(pair)
        exploded = explode(pair)
        if exploded != pair:
            pair = exploded
            continue
        splitted = split(pair)
        if splitted == pair:
            return pair
        pair = splitted

def find_magnitude(t):
    if isinstance(t.val, int):
        return t.val

    if t.val == ",":
        return 3 * find_magnitude(t.left) + 2 * find_magnitude(t.right)

def magnitude(pair):
    return find_magnitude(treeify(pair))

lines = [line.strip() for line in sys.stdin]
mag = 0
for (l1, l2) in product(lines, repeat=2):
    sum = "[" + l1 + ","  + l2 + ']'
    sum = reduce(sum)
    mag = max(mag, magnitude(sum))

print(mag)