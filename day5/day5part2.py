import itertools
from typing import Iterator

from day5 import find_lowest_location, parse_maps, split_input_into_sections


def parse_input_for_new_seed_format(seeds_section: str) -> Iterator[int]:
    seed_values = [
        int(seed_value) for seed_value in seeds_section.split(":")[1].split()
    ]

    seed_iterators = []
    for i in range(0, len(seed_values), 2):
        range_start = seed_values[i]
        range_length = seed_values[i + 1]
        seed_iterators.append(range(range_start, range_start + range_length))

    return itertools.chain(*seed_iterators)


def get_lowest_location_number(data: str) -> int:
    seeds_section, map_sections = split_input_into_sections(data)

    seeds = parse_input_for_new_seed_format(seeds_section)

    maps_dict = parse_maps(map_sections)

    return find_lowest_location(seeds, maps_dict)


def test():
    with open("test_input", "r") as f:
        data = f.read()
    output = get_lowest_location_number(data)
    print(output == 46, output)


def task():
    with open("input", "r") as f:
        data = f.read()
    output = get_lowest_location_number(data)
    print(output == 535088217, output)


if __name__ == "__main__":
    test()
    # task()
