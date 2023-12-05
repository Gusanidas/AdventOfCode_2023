from typing import Tuple

input_file = "../input/input_2.txt"

def get_set_contents(color_set: str) -> Tuple[int, int, int]:
    r = g = b = 0
    for color_box in color_set.split(","):
        number, color = color_box.strip().split(" ")
        if color == "red":
            r = int(number)
        elif color == "green":
            g = int(number)
        elif color == "blue":
            b = int(number)
    return r, g, b

def evaluate_set(set: str, r: int, g: int, b: int) -> bool:
    set_r, set_g, set_b = get_set_contents(set)
    return set_r<=r and set_g<=g and set_b<=b

def get_game_number(game_str) -> int:
    _, game_number = game_str.split(" ")
    return int(game_number)

def first_part():
    total = 0
    for line in open(input_file):
        game_str, sets_str = line.split(": ")
        game_number = get_game_number(game_str)
        if all([evaluate_set(set_str, 12, 13, 14) for set_str in sets_str.split("; ")]):
            total+=game_number
    return total

def get_minimum_power(sets_str: str) -> int:
    minr = ming = minb = 0
    for set_str in sets_str.split("; "):
        r, g, b = get_set_contents(set_str)
        minr = max(minr, r)
        ming = max(ming, g)
        minb = max(minb, b)
    return minr*ming*minb

def second_part():
    total = 0
    for line in open(input_file):
        game_str, sets_str = line.split(": ")
        min_power = get_minimum_power(sets_str)
        total+=min_power
    return total

print(f"part 1 answer: {first_part()}")
print(f"part 2 answer: {second_part()}")