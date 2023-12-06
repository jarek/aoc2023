from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


STEPS = [
    "seed",
    "soil",
    "fertilizer",
    "water",
    "light",
    "temperature",
    "humidity",
    "location",
]


@dataclass
class Range:
    destination_range_start: int
    source_range_start: int
    range_length: int

    def destination_for_source(self, source: int) -> Optional[int]:
        source_range_end = self.source_range_start + self.range_length
        if not (self.source_range_start <= source <= source_range_end):
            # input directly maps to output
            return None
        else:
            how_far_into_range = source - self.source_range_start
            return self.destination_range_start + how_far_into_range


@dataclass
class Map:
    resource_from: str
    resource_to: str
    ranges: List[Range]

    def destination_for_source(self, source: int) -> int:
        # TODO what happens when ranges overlap?

        for range in self.ranges:
            output = range.destination_for_source(source)
            if output is not None:
                return output

        # if no ranges match, input directly maps to output
        return source

    @classmethod
    def from_string(cls, map_str: str) -> "Map":
        map_lines = map_str.split("\n")
        map_name = map_lines[0]
        map_from, map_to = map_name.split("-to-")
        map_to = map_to.replace(" map:", "")

        map_ranges = [
            Range(*[int(num) for num in numbers.split()])
            for numbers in map_lines[1:]
            if numbers  # ignore empty lines
        ]

        return Map(resource_from=map_from, resource_to=map_to, ranges=map_ranges)


def parse_input(data: str) -> Tuple[List[int], Dict[str, Map]]:
    sections = data.split("\n\n")

    seeds = [int(seed_num) for seed_num in sections[0].split(":")[1].split()]

    maps = [Map.from_string(map_str) for map_str in sections[1:]]
    maps_dict = {map.resource_to: map for map in maps}

    return seeds, maps_dict


def get_lowest_location_number(data: str) -> int:
    seeds, maps_dict = parse_input(data)

    locations = []
    for seed in seeds:
        source_num = seed
        for step in STEPS[1:]:
            # after each step, the new destination becomes the new source_num
            source_num = maps_dict[step].destination_for_source(source_num)
        locations.append(source_num)

    return min(locations)


def test():
    with open("test_input", "r") as f:
        data = f.read()
    output = get_lowest_location_number(data)
    print(output == 35, output)


def task():
    with open("input", "r") as f:
        data = f.read()
    output = get_lowest_location_number(data)
    print(output == 535088217, output)


if __name__ == "__main__":
    test()
    task()
