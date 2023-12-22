from typing import List

board = []
for i, line in enumerate(open("../input/input_21.txt").readlines()):
    row = []
    for j, c in enumerate(line.strip()):
        if c == "S":
            start = (i,j)
            row.append(".")
        else:
            row.append(c)
    board.append(row)

def count_positions(board: List[List[str]], start: (int, int), steps: int, use_pattern = True)->int:
    r = [1]
    positions = set([start])
    prev = set()
    n = [(0,1),(1,0),(0,-1),(-1,0)]
    for i in range(steps):
        if use_pattern and len(positions) > 1000:
            r.append(r[-131]*2 - r[-131*2])
        else:
            new_positions = set()
            for pos in positions:
                for d in n:
                    new_pos = (pos[0]+d[0], pos[1]+d[1])
                    if new_pos in prev or new_pos in positions:
                        continue
                    if board[new_pos[0]%len(board)][new_pos[1]%len(board[0])] == ".":
                        new_positions.add(new_pos)
            prev = positions
            positions = new_positions
            r.append(len(positions))
    return r

r = count_positions(board, start, 64)
total = sum([x for i, x in enumerate(r) if i%2!=len(r)%2])
print(f"Part 1: {total}")

r = count_positions(board, start, 26501365)
total = sum([x for i, x in enumerate(r) if i%2!=len(r)%2])
print(f"Part 2: {total}")