
from typing import Tuple, List
from dataclasses import dataclass

@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int


def process_condition(condition: str):
    extra = 0
    if ">" in condition:
        a, b = condition.split(">")
        partial = lambda x: x > int(b)
        extra = 1 
    elif "<" in condition:
        a, b = condition.split("<")
        partial = lambda x: x < int(b)
    else:
        return lambda x: True
    if a == "a":
        return lambda x: partial(x.a)
    elif a == "m":
        return lambda x: partial(x.m)
    elif a == "s":
        return lambda x: partial(x.s)
    else:
        return lambda x: partial(x.x)

def process_rule(rule: str):
    #print(f"processing rule {rule}")
    key, value = rule.split("{")
    value = value.replace("}", "")
    rules = []
    for v in value.split(","):
        if ":" in v:
            a, b = v.split(":")
        else:
            a, b = "", v
        rules.append((process_condition(a), b))
    return key, rules

def process_part(part: str) -> Part:
    fields = part[1:-1].split(",")
    x, m, a, s = [f.split("=")[1] for f in fields]
    return Part(int(x), int(m), int(a), int(s))

def apply_workflow(part: Part, workflow: Tuple):
    for condition, rule in workflow:
        if condition(part):
            return rule

def run_workflows(part: Part):
    key = "in"
    while key not in ["A","R"]:
        workflow = rules[key]
        key = apply_workflow(part, workflow)

    return key == "A"


rules = {}
parts = []
for line in open("../input/input_19.txt").readlines():
    if line and line[0] == "{":
        parts.append(process_part(line.strip()))
    elif len(line)>2:
        rules.update([process_rule(line.strip())])

total = 0
for part in parts:
    if run_workflows(part):
        total += part.x+part.m+part.a+part.s

print(f"Part 1: {total}")