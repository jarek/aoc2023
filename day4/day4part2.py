from typing import List

from day4 import parse_line, count_matches, test_data


def add_up_card_copies(input: List[str]) -> int:
    initial_num_cards = len(input)

    card_copies = [1] * initial_num_cards

    for line in input:
        card = parse_line(line)
        score = count_matches(card)

        num_this_card = card_copies[card.number - 1]

        # print(f"card {card.number} has score {score} and we have {num_this_card} copies including original")

        for i in range(card.number + 1, card.number + 1 + score):
            if i <= initial_num_cards:
                # print(f"giving {num_this_card} copies of card {i}")
                card_copies[i - 1] += num_this_card

    return sum(card_copies)


def task():
    with open("input", "r") as f:
        data = f.readlines()
    output = add_up_card_copies(data)
    print(output == 14814534, output)


if __name__ == "__main__":
    output = add_up_card_copies(test_data)
    print(output == 30, output)
    task()
