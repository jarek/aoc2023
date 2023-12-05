from collections import defaultdict
from typing import Dict, List, Set

from day3 import (
    STAR,
    Position,
    Number,
    Symbol,
    build_map_near_symbols,
    find_numbers_and_symbols,
    test_data,
)


def get_symbols_near_result(
    result: Number, symbols: Dict[Position, List[Symbol]]
) -> Set[Symbol]:
    matching_symbols = set()
    for x in range(result.position.x, result.end_x + 1):
        check_position = Position(x=x, y=result.position.y)
        symbols_nearby = symbols[check_position]
        if symbols_nearby:
            matching_symbols.update(symbols_nearby)

    return matching_symbols


def add_up_gear_numbers(input: List[str]) -> int:
    numbers, symbols = find_numbers_and_symbols(input)

    map_near_symbols = build_map_near_symbols(symbols)

    # first find all numbers that are near stars (gears),
    # then filter to those that have 2 surrounding the same star

    numbers_and_their_nearby_symbols: Dict[Number, Set[Symbol]] = {
        number: get_symbols_near_result(number, map_near_symbols) for number in numbers
    }

    numbers_near_stars = {
        number: symbols
        for number, symbols in numbers_and_their_nearby_symbols.items()
        if any(symbol.symbol == STAR for symbol in symbols)
    }

    stars_to_nearby_numbers: Dict[Symbol, List[Number]] = defaultdict(list)
    for number, symbols in numbers_near_stars.items():
        for symbol in symbols:
            if symbol.symbol == STAR:
                stars_to_nearby_numbers[symbol].append(number)

    numbers_near_two_stars = [
        numbers for numbers in stars_to_nearby_numbers.values() if len(numbers) == 2
    ]

    total = 0
    for number_pair in numbers_near_two_stars:
        first_number = number_pair[0]
        second_number = number_pair[1]
        total += first_number.number * second_number.number

    return total


def task():
    with open("input", "r") as f:
        data = f.readlines()
    output = add_up_gear_numbers(data)
    print(output == 78236071, output)


if __name__ == "__main__":
    output = add_up_gear_numbers(test_data)
    print(output == 467835 + 610 * 7, output)
    task()
