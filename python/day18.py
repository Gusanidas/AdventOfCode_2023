def length_coordinates(coordinates):
    length = 0
    for i in range(len(coordinates)-1):
        length += abs(coordinates[i][0] - coordinates[i+1][0]) + abs(coordinates[i][1] - coordinates[i+1][1])
    return length


def polygon_area(coordinates):
    n = len(coordinates)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += coordinates[i][0] * coordinates[j][1]
        area -= coordinates[j][0] * coordinates[i][1]
    return abs(area) / 2.0

def area_coordinates(coordinates):
    return polygon_area(coordinates)+length_coordinates(coordinates)//2+1


def next_position(pos, d, a):
    if d == "U":
        return (pos[0]-a, pos[1])
    elif d == "D":
        return (pos[0]+a, pos[1])
    elif d == "L":
        return (pos[0], pos[1]-a)
    elif d == "R":
        return (pos[0], pos[1]+a)


first_part_data = []
second_part_data = []
filename = "../input/input_18.txt"
for line in open(filename, 'r'):
    d, a, color = line.strip().split(' ')
    first_part_data.append((d, int(a)))
    a = int(color[2:-2],16)
    d = {0: "R", 1: "D", 2: "L", 3: "U"}[int(color[-2])]
    second_part_data.append((d, a))

coordinates = [(0,0)]
for d, a in first_part_data:
    coordinates.append(next_position(coordinates[-1], d, a))

print(f"Part 1: {area_coordinates(coordinates)}")

coordinates = [(0,0)]
for d, a in second_part_data:
    coordinates.append(next_position(coordinates[-1], d, a))

print(f"Part 2: {area_coordinates(coordinates)}")