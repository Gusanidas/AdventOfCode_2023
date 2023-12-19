import re
instr = ""
map = dict()
for i, line in enumerate(open('../input/input_8.txt')):
    if i == 0:
        instr = line.strip()
    elif i>1:
        match = re.match(r"(\w+) = \((\w+), (\w+)\)", line)
        if match:
            a,b,c = match.groups()
            if a.endswith("Z") or b.endswith("Z") or c.endswith("Z"):
                print(f"found {a}, {b}, {c}")
            map[a] = (b,c)

idx = 0
curr = "AAA"
steps = 0
while curr != "ZZZ":
    d = 0 if instr[idx]=="L" else 1
    curr = map.get(curr, "ZZZ")[d]
    idx = (idx+1)%len(instr)
    steps += 1
    if steps>100000:
        break

print(f"first part solution = {steps}")

starting, ending, cicle = set(), set(), dict()
idx = 0
for k in map.keys():
    if k.endswith("A"):
        starting.add(k)
    elif k.endswith("Z"):
        ending.add(k)
    curr = k
    for ins in instr:
        d = 0 if ins=="L" else 1
        curr = map.get(curr, "ZZZ")[d]
    cicle[k] = curr

node_circles = []
for curr in starting:
    initial = curr
    steps = 0
    while curr not in ending:
        steps += 1
        curr = cicle[curr]
    first_steps = steps
    curr = cicle[curr]
    steps += 1
    while curr not in ending:
        steps += 1
        curr = cicle[curr]
    circle_steps = steps-first_steps
    node_circles.append((initial, curr, first_steps, circle_steps))


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def mcm(a, b):
    return a*b//gcd(a,b)


def merge_steps(f1, c1, f2, c2):
    s1, s2 = f1, f2
    while s1 != s2:
        if s1<s2:
            s1 += c1
        else:
            s2 += c2
    return s1, mcm(c1, c2)

f, c = 0, 1
for node, ending_node,  f1, c1 in node_circles:
    f, c = merge_steps(f, c, f1, c1)

print(f"f = {f}, c = {c}")
print(f"second part solution = {f*len(instr)}")

