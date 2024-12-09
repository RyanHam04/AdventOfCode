from day8_part1 import read_data, create_character_locations
from typing import Dict, Tuple, List, Set
from math import gcd


def calculate_line_of_antinodes(
    all_locations: Dict[str, List[Tuple[int, int]]],
    data: List[List[str]],
) -> Set[Tuple[int, int]]:
    """
    Instead of a single antinode, this function generates a
    line of antinodes, based on y = (dy/dx)*x + b, so there is
    a diagonal of antinodes, both on the upper boundary and lower boundary.


    Args:
        all_locations (Dict[str, List[Tuple[int, int]]]):
        A dictionary where the characters are the keys,
            and the coordinates are the values
        data (List[List[str]]): The data in a nested list.

    Returns:
        Set[Tuple[int, int]]: The set containing all antinodes,
        created in diagonals.
    """
    map_height = len(data)
    map_width = len(data[0])
    all_antinodes = set()

    for _, coordinates in all_locations.items():
        if len(coordinates) == 1:
            all_antinodes.add(coordinates[0])
            continue

        all_antinodes.update(coordinates)

        for i, (x1, y1) in enumerate(coordinates):
            for j in range(i + 1, len(coordinates)):
                x2, y2 = coordinates[j]

                dx = x2 - x1
                dy = y2 - y1
                common_divisor = abs(gcd(dx, dy))
                dx = dx // common_divisor
                dy = dy // common_divisor

                current_x, current_y = x1 + dx, y1 + dy
                while (0 <= current_x < map_width
                       and 0 <= current_y < map_height):
                    all_antinodes.add((current_x, current_y))
                    current_x += dx
                    current_y += dy

                current_x, current_y = x1 - dx, y1 - dy
                while (0 <= current_x < map_width
                       and 0 <= current_y < map_height):
                    all_antinodes.add((current_x, current_y))
                    current_x -= dx
                    current_y -= dy

    return all_antinodes


if __name__ == "__main__":
    data = read_data("2024/inputs/Assignment8_input.txt")
    locations = create_character_locations(data)
    result = calculate_line_of_antinodes(locations, data)

    print(len(result))
