from typing import List

seen = dict()
def number_of_arrangements(springs: str, contiguous: List[int]) -> int:
    if len(contiguous) == 0:
        return 1 if all([x!="#" for x in springs]) else 0
    if len(springs)==0:
        return 0
    if (springs, tuple(contiguous)) in seen:
        return seen[(springs, tuple(contiguous))]
    idx, r = 0, 0
    while idx<len(springs) and springs[idx] not in ["?","#"]:
        idx += 1
    if contiguous[0]<= len(springs)-idx:
        if springs[idx] != "#":
            r += number_of_arrangements(springs[idx+1:], contiguous)
        if all([x in ["#","?"] for x in springs[idx: idx+contiguous[0]]]) and (len(springs)==idx+contiguous[0] or springs[idx+contiguous[0]]!="#"):
            r += number_of_arrangements(springs[idx+contiguous[0]+1:], contiguous[1:])
    seen[(springs, tuple(contiguous))] = r
    return r

def add_more(springs, contiguous):
    new_springs = springs +"?"+springs +"?"+springs +"?"+springs +"?"+springs
    return new_springs,contiguous*5

total = 0
for line in open("../input/input_12.txt"):
    springs, cont = line.strip().split(" ")
    cont = [int(x) for x in cont.split(",")]
    total += number_of_arrangements(springs, cont)

print(f"First part solution = {total}")

total = 0
for line in open("../input/input_12.txt"):
    springs, cont = line.strip().split(" ")
    cont = [int(x) for x in cont.split(",")]
    springs, cont = add_more(springs, cont)
    total += number_of_arrangements(springs, cont)

print(f"Second part solution = {total}")