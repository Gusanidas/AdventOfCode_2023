from typing import List


def extrapolate_and_diff(x: List[int])->int:
    if all([xx==0 for xx in x]):
        return 0
    else:
        new_x = [x2 - x1 for x1, x2 in zip(x, x[1:])]
        return extrapolate_and_diff(new_x)+x[-1]

filename = "../input/input_9.txt"

total = 0
for line in open(filename):
    total += extrapolate_and_diff([int(x) for x in line.split(" ")])

print(f"First part solution = {total}")

total = 0
for line in open(filename):
    total += extrapolate_and_diff([int(x) for x in reversed(line.split(" "))])

print(f"Second part solution = {total}")