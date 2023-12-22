import functools
from typing import Tuple
from collections import deque, OrderedDict

conjuction_input = OrderedDict()
conjuction_activated = OrderedDict()
flipflop_states = OrderedDict()
node_out = OrderedDict()

for line in open("../input/input_20.txt"):
    sender, receiver = line.strip().split(" -> ")
    output_nodes = [out.strip() for out in receiver.split(",")]
    sender = sender.strip()
    if sender[0] == "b":
        node_out["broadcast"] = output_nodes
    elif sender[0] == "%":
        node_out[sender[1:]] = output_nodes
        flipflop_states[sender[1:]] = 0
    elif sender[0] == "&":
        node_out[sender[1:]] = output_nodes
        conjuction_input[sender[1:]] = dict()
        conjuction_activated[sender[1:]] = 0

for sender, receiver_list in node_out.items():
    for receiver in receiver_list:
        if receiver in conjuction_input:
            conjuction_input[receiver][sender] = False

def process_pulse(pulse: Tuple[bool, str, str], pulses: deque):
    type, sender, receiver = pulse
    if receiver == "broadcast":
        for receiver in node_out["broadcast"]:
            pulses.append((type, sender, receiver)) 
    elif receiver in conjuction_input:
        conjuction_activated[receiver] += type and not conjuction_input[receiver][sender]
        conjuction_activated[receiver] -= not type and conjuction_input[receiver][sender]
        conjuction_input[receiver][sender] = type
        sending_type = conjuction_activated[receiver] != len(conjuction_input[receiver])
        for out_n in node_out[receiver]:
            pulses.append((sending_type, receiver, out_n))
    elif receiver in flipflop_states:
        flipflop_states[receiver] = type == flipflop_states[receiver]
        if not type:
            for out_n in node_out[receiver]:
                pulses.append((flipflop_states[receiver], receiver, out_n))

def process_button(counter, vip_nodes = dict(), iteration = 0):
    pulses = deque([(False, "buttom", "broadcast")])
    while len(pulses) > 0:
        pulse = pulses.popleft()
        counter[pulse[0]] += 1
        process_pulse(pulse, pulses)
        if pulse[2] in vip_nodes and not pulse[0]:
            vip_nodes[pulse[2]].append(iteration)

counter = [0,0]
for i in range(1000):
    process_button(counter)

print(f" part one = {counter[0]*counter[1]}")

vip_nodes = {"rk": [], "cd": [], "zf": [], "qx": []}
iteration = 0
while any([len(v) < 2 for v in vip_nodes.values()]):
    process_button(counter, vip_nodes = vip_nodes, iteration = iteration)
    iteration += 1

total = functools.reduce(lambda x,y: x*y, [v[-1]-v[-2] for v in vip_nodes.values()], 1)
print(f" part two = {total}")