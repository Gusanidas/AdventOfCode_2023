from queue import Queue

s, map = None, dict()
maxi, maxj = 0, 0
for i, line in enumerate(open('../input/input_10.txt')):
    maxi = max(maxi, i)
    for j, c in enumerate(line):
        #print(f"i = {i}, j = {j}, c = {c}")
        if c != " ":
            maxj = max(maxj, j)
        if c == "-":
            map[(i,j)] = [(i,j-1), (i,j+1)]
        elif c == "|":
            map[(i,j)] = [(i-1,j), (i+1,j)]
        elif c == "F":
            map[(i,j)] = [(i+1,j), (i,j+1)]
        elif c == "L":
            map[(i,j)] = [(i-1,j), (i,j+1)]
        elif c == "7":
            map[(i,j)] = [(i+1,j), (i,j-1)]
        elif c == "J":
            map[(i,j)] = [(i-1,j), (i,j-1)]
        elif c == "S":
            starting = (i, j)
            map[(i,j)] = [(i-1,j), (i,j+1), (i+1,j),(i,j-1)]


loop = [starting]
prev = starting
while True:
    curr = loop[-1]
    for node in map.get(curr, []):
        if 0<=node[0]<=maxi and 0<=node[1]<=maxj and node!=prev and curr in map.get(node, []):
            loop.append(node)
            prev = curr
            break
    if loop[-1] == starting:
        break

print(f"First part solution = {(len(loop)-1)//2}")

loop_set = set(loop)

def triple(i, j, a):
    if a:
        return [(i-1,j),(i,j),(i+1,j)]
    else:
        return [(i,j-1),(i,j),(i,j+1)]

def get_dir(p1, p2):
    i,j = p1
    x, y = p2
    d1,d2 = x-i, y-j
    if (d1,d2) == (0,1):
        return triple(i-1,j,False), triple(i+1,j, False)
    elif (d1, d2) == (0,-1):
        return triple(i+1,j, False), triple(i-1,j, False)
    elif (d1, d2) == (1,0):
        return triple(i,j+1, True), triple(i,j-1, True)
    elif (d1, d2) == (-1,0):
        return triple(i,j-1, True), triple(i,j+1, True)
    else:
        raise ValueError(f"d1 = {d1}, d2 = {d2}")

l, r = set(), set()
for i, (li,lj) in enumerate(loop[1:]):
    lepp, repp = get_dir(loop[i],(li, lj))
    for lep in lepp:
        if lep not in loop_set and lep not in r and 0<=lep[0]<=maxi and 0<lep[1]<=maxj:
            l.add(lep)
    for rep in repp:
        if rep not in loop_set and rep not in l and 0<=rep[0]<=maxi and 0<rep[1]<=maxj:
            r.add(rep)

def get_neighbours(p):
    i, j = p
    r = []
    for ri, rj in [(i+1, j),(i-1,j),(i,j-1),(i,j+1),(i+1,j+1),(i+1,j-1),(i-1,j+1),(i-1,j-1)]:
        if (ri, rj) not in loop_set and 0<=ri<=maxi and 0<=rj<=maxj:
            r.append((ri, rj))
    return r

while True:
    new_l, new_r = set(), set()
    for p in l:
        for n in get_neighbours(p):
            if n not in r and n not in l:
                new_l.add(n)
    for p in r:
        for n in get_neighbours(p):
            if n not in r and n not in l:
                new_r.add(n)
    if len(new_l) + len(new_r)<1:
        break
    l = l.union(new_l)
    r = r.union(new_r)

inside = l if (0,5) in r else r
print(f"Second part solution = {len(inside)}")


