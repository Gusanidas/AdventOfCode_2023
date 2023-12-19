
universe = []
rows = set()
cols = set()
for i,line in enumerate(open("../input/input_11.txt")):
    universe.append(list(line.strip()))
    if "#" not in line:
        rows.add(i)

for j in range(len(universe[0])):
    if "#" not in [row[j] for row in universe]:
        cols.add(j)

def difference(a, b, weight=1):
    horizontal = abs(a[0]-b[0])
    for i in range(min(a[0], b[0])+1, max(a[0], b[0])):
        if i in rows:
            horizontal += weight
    vertical = abs(a[1]-b[1])
    for j in range(min(a[1], b[1])+1, max(a[1], b[1])):
        if j in cols:
            vertical += weight
    return horizontal + vertical

stars = []
for i, row in enumerate(universe):
    for j, c in enumerate(row):
        if c == "#":
            stars.append((i,j))

total = 0
for i, star in enumerate(stars[:-1]):
    for j, other in enumerate(stars[i+1:]):
        total += difference(star, other)


print(f"First part solution = {total}")

total = 0
for i, star in enumerate(stars[:-1]):
    for j, other in enumerate(stars[i+1:]):
        total += difference(star, other, weight=999999)


print(f"Second part solution = {total}")