from typing import List, Tuple


MAX_VALUES = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def parse_draw(draw_text: str) -> dict:
    split_draw = draw_text.split(",")

    parsed_draw = {}
    for draw_entry in split_draw:
        count, colour = draw_entry.strip().split()
        parsed_draw[colour] = int(count)
    return parsed_draw


def parse_game(game_text: str) -> Tuple[int, List[dict]]:
    game_number, game_draws = game_text.split(":")

    game_number = int(game_number.replace("Game ", ""))

    split_draws = game_draws.split(";")

    parsed_draws = [parse_draw(draw_text) for draw_text in split_draws]

    return game_number, parsed_draws


def is_draw_possible(parsed_draw: dict) -> bool:
    return all([count <= MAX_VALUES[colour] for colour, count in parsed_draw.items()])


def is_game_possible(parsed_draws: List[dict]) -> bool:
    valid_draws = [draw for draw in parsed_draws if is_draw_possible(draw)]
    return len(valid_draws) == len(parsed_draws)


def add_up_possible_games(games: List[str]) -> int:
    possible_game_ids = []
    for game_text in games:
        game_num, parsed_draws = parse_game(game_text)
        if is_game_possible(parsed_draws):
            possible_game_ids.append(game_num)
    return sum(possible_game_ids)


test_data = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]

print(add_up_possible_games(test_data))


def task():
    with open("input", "r") as f:
        texts = f.readlines()
    print(add_up_possible_games(texts))


task()
