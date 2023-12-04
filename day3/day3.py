from collections import defaultdict
from dataclasses import dataclass
from typing import Any, Dict, List, Tuple


SPACER = "."


@dataclass(frozen=True)
class Position:
    y: int
    x: int


@dataclass
class Result:
    number: int
    position: Position
    end_x: int  # TODO also Position?


def tokenize_line(line: str) -> List[str]:
    line = line.strip()  # input from readlines() has \n characters

    results = []
    line_length = len(line)

    x = 0
    while x < line_length:
        char = line[x]
        sequence = char

        while char.isdigit():
            char = line[x + 1] if x < (line_length - 1) else ""

            if char.isdigit():
                sequence += char
                x += 1

        results.append(sequence or char)

        x += 1

    return results


def build_map_near_symbols(
    symbols: Dict[Position, str]
) -> Dict[Position, List[Position]]:
    result: Dict[Position, List[Position]] = defaultdict(list)

    for orig in symbols.keys():
        up = orig.y - 1
        down = orig.y + 1
        can_go_up = up >= 0
        left = orig.x - 1
        right = orig.x + 1
        can_go_left = left >= 0

        # note: we're not checking if we can go down or to the right,
        # because overflowing on those has no ill effect - we assume we always can

        if can_go_up:
            result[Position(x=orig.x, y=up)].append(orig)
            result[Position(x=right, y=up)].append(orig)
            if can_go_left:
                result[Position(x=left, y=up)].append(orig)

        # going down
        result[Position(x=orig.x, y=down)].append(orig)
        result[Position(x=right, y=down)].append(orig)
        if can_go_left:
            result[Position(x=left, y=down)].append(orig)

        if can_go_left:
            result[Position(x=left, y=orig.y)].append(orig)
            result[Position(x=left, y=down)].append(orig)
            if can_go_up:
                result[Position(x=left, y=up)].append(orig)

        # going right
        result[Position(x=right, y=orig.y)].append(orig)
        result[Position(x=right, y=down)].append(orig)
        if can_go_up:
            result[Position(x=right, y=up)].append(orig)

    return result


def find_numbers_and_symbols(
    input: List[str],
) -> Tuple[List[Result], Dict[Position, str]]:
    results = []
    symbols = {}
    for y, line in enumerate(input):
        line_parts = tokenize_line(line)
        # line_parts now looks like ['7', '.', '.', '$', '.', '*', '.', '.', '.', '.']
        # given input "7..$.*...."

        x = 0
        for part in line_parts:
            if part.isnumeric():
                part_length = len(part)
                end_x = x + part_length - 1
                # minus 1 to get "start position" of the last character in part

                results.append(
                    Result(number=int(part), position=Position(x=x, y=y), end_x=end_x)
                )
                x += part_length - 1  # skip to the end of the part
            elif part != SPACER:
                # save the fact that there's a symbol here
                # assumes any other symbol is single-character, otherwise we'd do `x += part_length` here too
                symbols[Position(x=x, y=y)] = part

            x += 1

    return results, symbols


def is_position_near_symbol(result: Result, symbols: Dict[Position, Any]) -> bool:
    for x in range(result.position.x, result.end_x + 1):
        if Position(x=x, y=result.position.y) in symbols:
            return True

    return False


def add_up_part_numbers(input: List[str]) -> int:
    numbers, symbols = find_numbers_and_symbols(input)

    map_near_symbols = build_map_near_symbols(symbols)

    numbers_near_symbols = [
        number
        for number in numbers
        if is_position_near_symbol(number, map_near_symbols)
    ]

    return sum(n.number for n in numbers_near_symbols)


test_data = [
    "467..114..\n",
    "...*......\n",
    "..35..633.\n",
    "......#...\n",
    "610*7.....\n",  # note: changed to highlight a bug - was `617*......`
    ".....+.58.\n",
    "..592.....\n",
    "......755.\n",
    "7..$.*....\n",  # note: changed from test input, but doesn't change result
    ".664.598..\n",
    "..........\n",
    "./663.273.\n",  # note: added from scratch to highlight another edge case
]


def task():
    with open("input", "r") as f:
        data = f.readlines()
    output = add_up_part_numbers(data)
    print(output == 533775, output)


if __name__ == "__main__":
    output = add_up_part_numbers(test_data)
    print(output == 4361 + 663, output)
    task()
