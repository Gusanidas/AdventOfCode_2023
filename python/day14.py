def roll_rocks(old_s):
    p, r, s = 0, 0, 0
    a = []
    for c in old_s:
        if c == '#':
            s += 1
        elif c == '.':
            if s: a.append((p, r, s)); p, r, s = 0, 0, 0
            p += 1
        else:
            if s: a.append((p, r, s)); p, r, s = 0, 0, 0
            r += 1
    a.append((p, r, s))
    return list(''.join('.' * p + 'O' * r + '#' * s for p, r, s in a))

def transpose(board):
    return [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]

def roll_east(board):
    return [roll_rocks(row) for row in board]

def roll_west(board):
    return [roll_rocks(row[::-1])[::-1] for row in board]

def roll_south(board):
    board = [roll_rocks([board[j][i] for j in range(len(board))]) for i in range(len(board[0]))]
    return transpose(board)

def roll_north(board):
    board = [roll_rocks([board[j][i] for j in range(len(board))][::-1])[::-1] for i in range(len(board[0]))]
    return transpose(board) 

def get_hash(board):
    return "".join(["".join(line) for line in board])

mem_1 = dict()
def cycle(board):
    key = get_hash(board) 
    if key in mem_1:
        return mem_1[key]
    board = roll_north(board)
    board = roll_west(board)
    board = roll_south(board)
    board = roll_east(board)
    mem_1[key] = board
    return board

mem_10k = dict()
def cycle_10k(board):
    key = get_hash(board)
    if key in mem_10k:
        return mem_10k[key]
    for i in range(10000):
        board = cycle(board)
    mem_10k[key] = board
    return board

def total_load(board):
    return sum([sum([len(board)-j if board[j][i] == "O" else 0 for j in range(len(board))]) for i in range(len(board[0]))])

board = []
for line in open("../input/input_14.txt"):
    board.append(list(line.strip()))

board = roll_north(board)
print(f"First part = {total_load(board)}")

for i in range(100000):
    board = cycle_10k(board)

print(f"Second part = {total_load(board)}")