def le_hash(s):
    t = 0
    for c in s:
        t = ((t+ord(c))*17)%256
    return t

hash_map = [[] for i in range(256)]
def process_eq(t, tag, value):
    seen = False
    for lense in hash_map[t]:
        if lense[0] == tag:
            lense[1] = int(value)
            seen = True
            break
    if not seen:
        hash_map[t].append([tag, int(value)])

def process_dash(t, tag):
    for lense in hash_map[t]:
        if lense[0] == tag:
            hash_map[t].remove(lense)
            break

def process_tag(s):
    if "=" in s:
        tag, value = s.split("=")
        t = le_hash(tag)
        process_eq(t, tag, value)
    else:
        t = le_hash(s[:-1])
        process_dash(t, s[:-1])
t = 0
for line in open("../input/input_15.txt"):
    for c in line.strip().split(","):
        t += le_hash(c)

print(f"First part = {t}")

t = 0
for line in open("../input/input_15.txt"):
    for c in line.strip().split(","):
        process_tag(c)

for i, box in enumerate(hash_map):
    for j, (tag, value) in enumerate(box):
        t += (i+1)*(j+1)*value

print(f"Scond part = {t}")