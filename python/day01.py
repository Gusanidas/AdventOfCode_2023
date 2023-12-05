from typing import Optional, Callable

digits = {
    **dict(zip("0123456789", range(10))),
    **dict(
        zip(
            [
                "zero",
                "one",
                "two",
                "three",
                "four",
                "five",
                "six",
                "seven",
                "eight",
                "nine",
            ],
            range(10),
        )
    ),
}


def get_number_part_1(s: str) -> int:
    first, last = None, None
    for i, c in enumerate(s):
        if c in digits:
            if not first:
                first = c
            last = c
    return int(first + last)

def get_total(get_number: Callable) -> int:
    total = 0
    with open('../input/input_1.txt') as file:
        for line in file:
            total += get_number(line)
    return total

def get_digit(s: str, i: int) -> Optional[int]:
    for key in digits:
        if s[i:].startswith(key):
            return digits[key]
    return None

def get_number_part_2(s: str) -> int:
    first, last = None, None
    for i, _ in enumerate(s):
        c = get_digit(s, i)
        if c:
            if not first:
                first = c
            last = c
    return 10 * first + last


print(f"part 1 answer: {get_total(get_number_part_1)}")
print(f"part 2 answer: {get_total(get_number_part_2)}")
