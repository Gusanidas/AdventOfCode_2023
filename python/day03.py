from typing import List, Set, Dict, Tuple

board: List[List[str]] = []

with open('../input/input_3.txt', 'r') as file:
    for line in file:
        board.append(list(line.strip()))

digits: Set[str] = set("0123456789")

def neighbouring_symbol(board: List[List[str]], i: int, j: int) -> bool:
    neigh = [(i-1, j), (i+1, j), (i, j-1), (i, j+1), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]
    for x, y in neigh:
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            continue
        if board[x][y] != "." and board[x][y] not in digits:
            return True
    return False

def part_one():
    total = 0
    curr = ""
    should_add = False
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if x not in digits:
                if len(curr)>0 and should_add:
                    total+=int(curr)
                should_add = False
                curr = ""
            elif x in digits:
                curr+=x
                should_add |= neighbouring_symbol(board, i, j)
        if len(curr)>0 and should_add:
            total+=int(curr)
        should_add = False
        curr = ""
    return total

def neighbouring_gear(board: List[List[str]], i: int, j: int) -> Set[Tuple[int, int]]:
    r = set()
    neigh = [(i-1, j), (i+1, j), (i, j-1), (i, j+1), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]
    for x, y in neigh:
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            continue
        if board[x][y] == "*":
            r.add((x, y))
    return r

def add_gears(gears: Dict[Tuple[int, int], List[str]], should_add: Set[Tuple[int, int]], curr: str) -> None:
    for x, y in should_add:
        if (x, y) not in gears:
            gears[(x, y)] = []
        gears[(x, y)].append(curr)

def part_two():
    total = 0
    curr = ""
    should_add = set()
    gears = dict()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if x not in digits:
                if len(curr)>0 and len(should_add)>0:
                    add_gears(gears, should_add, curr)
                should_add = set()
                curr = ""
            elif x in digits:
                curr+=x
                should_add.update(neighbouring_gear(board,i,j))
        if len(curr)>0 and should_add:
            add_gears(gears, should_add, curr)
        should_add = set()
        curr = ""

    for k, v in gears.items():
        if len(v) == 2:
            vl = list(v)
            val = int(vl[1])*int(vl[0])
            total += val

    return total

print(f"part 1 answer: {part_one()}")
print(f"part 2 answer: {part_two()}")