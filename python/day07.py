from typing import Tuple
from collections import Counter
from dataclasses import dataclass
from enum import Enum

class CardValue(Enum):
    A = 16
    K = 15
    Q = 14
    J = 13
    T = 12
    nine = 9
    eight = 8
    seven = 7
    six = 6
    five = 5
    four = 4
    three = 3
    two = 2
    Joker = 1


    def __lt__(self, other):
        # Define the custom ordering
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

@dataclass(order=True)
class Hand():
    hand_value: int
    cards: Tuple[CardValue,...]
    hand_string: str
    

    hand_values = {(1,1,1,1,1): 1, (2,1,1,1):2, (2,2,1):3, (3,1,1):4, (3,2):5, (4,1):6, (5,): 7}

    @classmethod
    def new_hand(cls, hand_string: str, card_values: dict) -> "Hand":
        card_values = [card_values[card] for card in hand_string]
        hand_value = cls.get_hand_value(card_values)
        return cls(hand_value, tuple(card_values), hand_string)

    @classmethod
    def get_hand_value(cls, cards) -> int:
        counter = Counter(cards)
        jf = 0
        if CardValue.Joker in counter:
            if counter[CardValue.Joker] <5:
                jf = counter[CardValue.Joker]
                counter.pop(CardValue.Joker)
        
        freq = sorted(counter.values(), reverse=True)
        freq[0]+=jf
        hand_value = cls.hand_values[tuple(freq)]
        return hand_value

    def __repr__(self):
        return self.hand_string

def process_file(filename, card_values):
    hands = []
    with open(filename) as file:
        for line in file:
            hand_str, bid_str = line.split(" ")
            hands.append((Hand.new_hand(hand_str, card_values), int(bid_str)))
    return hands

def calculate_total(hands):
    total = 0
    for i, (hand, bid) in enumerate(sorted(hands)):
        total += bid*(i+1)
    return total

card_values_1 = {"A": CardValue.A, "K": CardValue.K, "Q": CardValue.Q, "J": CardValue.J, "T": CardValue.T, "9": CardValue.nine, "8": CardValue.eight, "7": CardValue.seven,
    "6": CardValue.six, "5": CardValue.five, "4": CardValue.four, "3": CardValue.three, "2": CardValue.two}
card_values_2 = {"A": CardValue.A, "K": CardValue.K, "Q": CardValue.Q, "J": CardValue.Joker, "T": CardValue.T, "9": CardValue.nine, "8": CardValue.eight, "7": CardValue.seven,
    "6": CardValue.six, "5": CardValue.five, "4": CardValue.four, "3": CardValue.three, "2": CardValue.two}

hands = process_file("../input/input_7.txt", card_values_1)
total = calculate_total(hands)
print(f"First part answer = {total}")

hands = process_file("../input/input_7.txt", card_values_2)
total = calculate_total(hands)
print(f"Second part answer = {total}")
