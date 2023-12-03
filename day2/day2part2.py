from collections import defaultdict
from typing import List

from day2 import parse_game, test_data


def determine_game_power(parsed_draws: List[dict]) -> int:
    minimum_colour_count = defaultdict(int)
    for parsed_draw in parsed_draws:
        for colour, count in parsed_draw.items():
            minimum_colour_count[colour] = max(count, minimum_colour_count[colour])

    power = 1
    for count in minimum_colour_count.values():
        power *= count

    return power


def add_up_game_powers(games: List[str]) -> int:
    game_powers = []
    for game_text in games:
        _, parsed_draws = parse_game(game_text)
        game_power = determine_game_power(parsed_draws)
        game_powers.append(game_power)

    return sum(game_powers)


def task():
    with open("input", "r") as f:
        texts = f.readlines()
    print(add_up_game_powers(texts))


if __name__ == "__main__":
    print(add_up_game_powers(test_data))
    task()
