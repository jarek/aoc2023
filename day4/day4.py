import math
from dataclasses import dataclass
from typing import List, Set


@dataclass
class Card:
    number: int
    winning_numbers: Set[int]
    own_numbers: Set[int]


def parse_line(line: str) -> Card:
    card_number, numbers = line.split(":")
    card_number = card_number.replace("Card ", "")
    card_number = int(card_number)

    winning_numbers, own_numbers = numbers.split("|")
    winning_numbers = set(map(int, winning_numbers.split()))
    own_numbers = set(map(int, own_numbers.split()))

    return Card(
        number=card_number, winning_numbers=winning_numbers, own_numbers=own_numbers
    )


def count_matches(card: Card) -> int:
    matching_numbers = card.winning_numbers & card.own_numbers

    return len(matching_numbers)


def score_card(card: Card) -> int:
    num_matching = count_matches(card)

    score = int(math.pow(2, num_matching - 1))

    return score


def add_up_points(input: List[str]) -> int:
    total = 0
    for line in input:
        card = parse_line(line)
        score = score_card(card)
        total += score

    return total


test_data = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\n",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\n",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\n",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\n",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\n",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11\n",
]


def task():
    with open("input", "r") as f:
        data = f.readlines()
    output = add_up_points(data)
    print(output == 33950, output)


if __name__ == "__main__":
    output = add_up_points(test_data)
    print(output == 13, output)
    task()
