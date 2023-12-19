from typing import Tuple, List
from functools import reduce

letter2idx = {"x": 0, "m": 1, "a": 2, "s": 3}
def apply_condition(condition , intervals: List[Tuple[int, int]])->List[Tuple[int, int]]:
    r = []
    c, letter, limit = condition
    for interval in intervals:
        v1, v2 = interval[letter2idx[letter]]
        if c:
            if v2 > limit+1:
                new_interval = [ii for ii in interval]
                new_interval[letter2idx[letter]] = (max(v1, limit+1), v2)
                r.append(tuple(new_interval))
        else:
            if v1 < limit:
                new_interval = [ii for ii in interval]
                new_interval[letter2idx[letter]] = (v1, min(v2, limit))
                r.append(tuple(new_interval))
    return r

def apply_conditions(conditions: List[str], intervals: List[Tuple[int, int]])->List[Tuple[int, int]]:
    r = intervals[:]
    for condition in conditions:
        r = apply_condition(condition, r)
    return r

        
mem_interval = dict()
def get_workflow_intervals(key: str, workflows)->Tuple[Tuple[int, int]]:
    if key in ["R", "A"]:
        return [((0,0), (0,0), (0,0), (0,0))] if key == "R" else [((1,4001), (1,4001), (1,4001), (1,4001))]
    else:
        if key in mem_interval:
            return mem_interval[key]
        else:
            r = []
            workflow = workflows[key]
            conditions = []
            for (c1, c2), key in workflow:
                r += apply_conditions([c1]+conditions, get_workflow_intervals(key, workflows)) 
                conditions.append(c2)
            mem_interval[key] = r
            return r

def get_conditions(condtion_str: str):
    if "<" in condtion_str:
        letter, limit = condtion_str.split("<")
        return (False, letter, int(limit)), (True, letter, int(limit)-1)
    elif ">" in condtion_str:
        letter, limit = condtion_str.split(">")
        return (True, letter, int(limit)), (False, letter, int(limit)+1)
    else:
        return (True, "x", 0), (False, "x", 0)

def process_rule(rule: str)->Tuple[str, Tuple[Tuple[str, str], str]]:
    key, workflow = rule.split("{")
    workflow_raw = workflow[:-1].split(",")
    workflow = []
    for w in workflow_raw:
        if ":" in w:
            c1, c2 = w.split(":")
        else:
            c1, c2 = "", w
        workflow.append((get_conditions(c1), c2))
    return key, workflow

workflows = dict()
for line in open("../input/input_19.txt").readlines():
    if line and line[0] == "{":
        pass
    elif len(line)>2:
        key, workflow = process_rule(line.strip())
        workflows[key] = workflow

total = 0
intervals = get_workflow_intervals("in", workflows)
for interval in intervals:
    total += reduce(lambda x,y: x*(y[1]-y[0]), interval, 1)

print(f"total = {total}")


        