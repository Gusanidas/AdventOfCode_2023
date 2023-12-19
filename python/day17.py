from collections import deque, defaultdict

neigh = [(-1,0),(1,0),(0,-1),(0,1)]
def get_neighbours_1(pos, v, steps):
    r = []
    nv = (-v[0], -v[1])
    for n in neigh:
        new_steps = steps+1 if n == v else 0
        nx, ny = pos[0]+n[0], pos[1]+n[1]
        if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]) or new_steps > 2 or n == nv:
            continue
        r.append(((nx, ny), n, new_steps))
    return r

def get_neighbours_2(pos, v, steps):
    r = []
    nv = (-v[0], -v[1])
    for n in neigh:
        new_steps = steps+1 if n == v else 0
        nx, ny = pos[0]+n[0], pos[1]+n[1]
        if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]) or new_steps > 9 or n == nv:
            continue
        if steps < 3 and n!=v:
            continue
        r.append(((nx, ny), n, new_steps))
    return r


def lava_flow(get_neighbours, board):
    q = deque()
    seen = defaultdict(lambda: defaultdict(int))
    q.append(((0, 0), (0, 1), -1))
    seen[(0, 0)][((0, 1), -1)] = 0
    q.append(((0, 0), (1, 0), -1))
    seen[(0, 0)][((1, 0), -1)] = 0

    while len(q) > 0:
        pos, v, steps = q.popleft()
        heat = seen[pos][(v, steps)]
        for new_pos, new_v, new_steps in get_neighbours(pos, v, steps):
            delta_heat = int(board[new_pos[0]][new_pos[1]])
            if seen[new_pos][(new_v, new_steps)] == 0 or seen[new_pos][(new_v, new_steps)] > heat + delta_heat:
                seen[new_pos][(new_v, new_steps)] = heat + delta_heat
                q.append((new_pos, new_v, new_steps))

    return seen

board = []
for line in open("../input/input_17.txt").readlines():
    board.append(list(line.strip()))

seen = lava_flow(get_neighbours_1, board)
min_heat = min(seen[(len(board)-1, len(board[0])-1)].values())
print(f"Part 1: {min_heat}")

seen = lava_flow(get_neighbours_2, board)
min_heat = float("inf")
for k,v in seen[(len(board)-1, len(board[0])-1)].items():
    _, steps = k 
    if steps >3:
        min_heat = min(min_heat, v)

print(f"Part 2: {min_heat}")