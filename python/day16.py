from queue import Queue
board = []
for line in open("../input/input_16.txt").readlines():
    board.append(list(line.strip()))


speed_change = dict()

speed_change["\\"] = {(0, 1): [(1, 0)], (0, -1): [(-1, 0)], (1, 0): [(0, 1)], (-1, 0): [(0, -1)]}
speed_change["/"] = {(0, 1): [(-1, 0)], (0, -1): [(1, 0)], (1, 0): [(0, -1)], (-1, 0): [(0, 1)]}

speed_change["-"] = {(0, 1): [(0, 1)], (0, -1): [(0, -1)], (1, 0): [(0, 1), (0, -1)], (-1, 0): [(0, 1), (0, -1)]}
speed_change["|"] = {(1, 0): [(1, 0)], (-1, 0): [(-1, 0)], (0, 1): [(1, 0), (-1, 0)], (0, -1): [(1, 0), (-1, 0)]}

speed_change["."] = {(0, 1): [(0, 1)], (0, -1): [(0, -1)], (1, 0): [(1, 0)], (-1, 0): [(-1, 0)]}


def num_ene(pos, v):
    q = Queue()
    q.put((pos, v))
    seen = set()
    ene = set()
    while not q.empty():
        pos, v = q.get()
        new = (pos[0]+v[0], pos[1]+v[1])
        if (v,new) in seen or new[0] < 0 or new[0] >= len(board) or new[1] < 0 or new[1] >= len(board[0]):
            continue
        seen.add((v,new))
        ene.add(new)
        v = speed_change[board[new[0]][new[1]]][v]
        for new_v in v:
            q.put((new, new_v))
    return len(ene)
    
print(f"Part 1: {num_ene((0, -1), (0,1))}")

max_ene=0
for i in range(len(board)):
    max_ene = max(max_ene, num_ene((i, -1), (0,1)))
    max_ene = max(max_ene, num_ene((i, len(board[0])), (0,-1)))

for i in range(len(board[0])):
    max_ene = max(max_ene, num_ene((-1, i), (1,0)))
    max_ene = max(max_ene, num_ene((len(board), i), (-1,0)))

print(f"Part 2: {max_ene}")
