file_name = "../input/input_4.txt"
def get_members(s):
    return set([x for x in s.strip().split(" ") if len(x)>0])

total = 0
line_count = 0
for line in open(file_name):
    _, line = line.split(": ")
    p1, p2 = line.strip().split("|")
    s1, s2 = get_members(p1), get_members(p2)
    intersec = len(s1.intersection(s2))
    total += 2**(intersec-1) if intersec>0 else 0
    line_count += 1

print(f"part 1 answer: {total}")


scratch_mem = dict()
def process_scratch(s, i):
    if i in scratch_mem:
        return scratch_mem[i]
    _, s = s.split(": ")
    p1, p2 = line.strip().split("|")
    s1, s2 = get_members(p1), get_members(p2)
    intersec = len(s1.intersection(s2))
    scratch_mem[i] = intersec
    return intersec

pending = [1 for i in range(line_count)]
total = sum(pending)
for i, line in enumerate(open(file_name)):
    t = pending[i]
    if t == 0:
        break
    prox = process_scratch(line, i)
    pending[i+1:i+prox+1] = [x+t for x in pending[i+1:i+prox+1]]
    total += prox*t

print(f"part 2 answer: {total}")
