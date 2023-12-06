from dataclasses import dataclass
from typing import Dict, Iterator, List, Optional, Tuple

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


def split_input_into_sections(data: str) -> Tuple[str, List[str]]:
    sections = data.split("\n\n")
    return sections[0], sections[1:]


def parse_maps(map_sections: List[str]) -> Dict[str, Map]:
    maps = [Map.from_string(map_str) for map_str in map_sections]
    maps_dict = {map.resource_to: map for map in maps}
    return maps_dict


def find_lowest_location(seeds: Iterator[int], maps_dict: Dict[str, Map]) -> int:
    lowest_location = 99999999999
    for seed in seeds:
        source_num = seed
        for step in STEPS[1:]:
            # after each step, the new destination becomes the new source_num
            source_num = maps_dict[step].destination_for_source(source_num)

        lowest_location = min(lowest_location, source_num)

    return lowest_location


def get_lowest_location_number(data: str) -> int:
    seeds_section, map_sections = split_input_into_sections(data)

    seeds = (int(seed_num) for seed_num in seeds_section.split(":")[1].split())

    maps_dict = parse_maps(map_sections)

    return find_lowest_location(seeds, maps_dict)


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
