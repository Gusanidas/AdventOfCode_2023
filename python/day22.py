from collections import deque

def horizontal_overlap(brick1, brick2):
    return brick1[0][0] <= brick2[1][0] and brick1[1][0] >= brick2[0][0] and brick1[0][1] <= brick2[1][1] and brick1[1][1] >= brick2[0][1]

def brick_overlap(brick1, brick2):
    return horizontal_overlap(brick1, brick2) and brick1[0][2] <= brick2[1][2] and brick1[1][2] >= brick2[0][2]

def check_brick(brick, other_bricks):
    if brick[0][2] < 1:
        return False
    for other_brick in other_bricks[::-1]:
        if brick_overlap(brick, other_brick):
            return False
    return True

bricks = []
for line in open("../input/input_22.txt").readlines():
    left, right = line.strip().split("~")
    coords_left = [int(c) for c in left.split(",")]
    coords_right = [int(c) for c in right.split(",")]
    bricks.append((coords_left, coords_right))

bricks.sort(key=lambda x: x[0][2])
fallen_bricks = []
for i, brick in enumerate(bricks):
    while True:
        try_brick = ((brick[0][0], brick[0][1], brick[0][2]-1), (brick[1][0], brick[1][1], brick[1][2]-1))
        if check_brick(try_brick, fallen_bricks):
            brick = try_brick
        else:
            break
    fallen_bricks.append(brick)
bricks = fallen_bricks

supports = dict()
supported = dict()
for i, brick in enumerate(bricks[:-1]):
    for j, other_brick in enumerate(bricks[i+1:]):
        if horizontal_overlap(brick, other_brick):
            if brick[1][2] == other_brick[0][2]-1:
                supported[j+i+1] = supported.get(j+i+1, []) + [i]
                supports[i] = supports.get(i, []) + [j+i+1]


total = 0
for i, brick in enumerate(bricks):
    vapor = True
    for j in supports.get(i, []):
        if j in supported and len(supported[j]) == 1:
            vapor = False
            break
    total += vapor

print(f"Part 1: {total}")

total = 0
for i, brick in enumerate(bricks):
    fallen = set([i])
    q = deque([i])
    while len(q) > 0:
        curr = q.popleft()
        for j in supports.get(curr, []):
            if all([k in fallen for k in supported.get(j, [])]):
                q.append(j)
                fallen.add(j)
    total += len(fallen)-1 # -1 because we don't count the brick itself

print(f"Part 2: {total}")
