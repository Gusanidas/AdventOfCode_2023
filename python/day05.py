maps = []
digits = set("0123456789")

for i, line in enumerate(open('../input/input_5.txt')):
    if i==0:
        _, seed_str = line.split(": ")
        seeds = [int(x) for x in seed_str.strip().split(" ")]
    else:
        if line.strip().endswith("map:"):
            maps.append([])
        elif len(line)>3:
            maps[-1].append([int(x) for x in line.strip().split(" ")])

def get_location(seed):
    curr = seed
    for map in maps:
        for row in map:
            d, s, r = row
            if s<=curr<=s+r:
                curr = curr-s+d
                break
    return curr

print(f"First part  = {min([get_location(x) for x in seeds])}")

def process_ranges(r1, r2, d, s, r):
    s1, s2 = s, s+r-1

    d_start = max(r1, s1)
    d_end = min(r2, s2)
    d = (d_start-s+d, d_end-s+d) if d_start <= d_end else None 

    c1 = (r1, min(r2, s1 - 1)) if r1 < s1 else None
    c2 = (max(r1, s2 + 1), r2) if r2 > s2 else None

    return [x for x in [c1, c2] if x], [d] if d else []

def get_location_2(ranges):
    for map in maps:
        new_ranges = []
        for row in map:
            d, s, r = row
            old_ranges = []
            for r1, r2 in ranges:
                old, new = process_ranges(r1, r2, d, s, r)
                old_ranges.extend(old)
                new_ranges.extend(new)
            ranges = old_ranges
        ranges = new_ranges+ranges
    return ranges

seed_ranges = []
for i in range(0, len(seeds),2):
    seed_ranges.append((seeds[i], seeds[i]+seeds[i+1]))

print(f"Second part =  {min(get_location_2(seed_ranges), key=lambda x: x[0])[0]}")