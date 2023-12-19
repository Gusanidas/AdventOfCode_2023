from typing import List

def is_mirror(board, i):
    l, r = i-1,i
    while l>=0 and r<len(board) and board[l]==board[r]:
        l -= 1
        r += 1
    return l<0 or r>=len(board)

def is_almost_mirror(board, i):
    l, r = i-1,i
    diffs = 0
    while l>=0 and r<len(board):
        diffs += [a != b for a,b in zip(board[l],board[r])].count(True)
        if diffs>1:
            return False
        l -= 1
        r += 1
    return diffs == 1


def process_input(filename: str) -> List[List[str]]:
    r = []
    with open(filename) as f:
        curr = []
        for line in f:
            line = line.strip()
            if line:
                curr.append(line)
            else:
                r.append(curr)
                curr = []
    r.append(curr)
    return r

def transpose(board):
    return ["".join([board[j][i] for j in range(len(board))]) for i in range(len(board[0]))]


boards = process_input("../input/input_13.txt")

rows, cols = [], []
for board in boards:
    found = False
    for i in range(1,len(board)):
        if is_mirror(board,i):
            rows.append(i)
            found = True
            break
    if not found:
        board = transpose(board)
        for i in range(1,len(board)):
            if is_mirror(board,i):
                cols.append(i)
                break

total = 100*sum(rows)+sum(cols)
print(f"First part solution = {total}")

rows, cols = [], []
for board in boards:
    found = False
    for i in range(1,len(board)):
        if is_almost_mirror(board,i):
            rows.append(i)
            found = True
            break
    if not found:
        board = transpose(board)
        for i in range(1,len(board)):
            if is_almost_mirror(board,i):
                cols.append(i)
                break

total = 100*sum(rows)+sum(cols)
print(f"Second part solution = {total}")