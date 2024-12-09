from typing import List, Dict, Set, Tuple


def read_data(file_path: str) -> List[List[str]]:
    """Used for reading the data into a format thats
    convenient for the assignment of day 8

    Args:
        file_path (str): The directory of the file containing the data (.txt)

    Returns:
        all_data (List[List[str]]): Nested list containing the data
    """
    all_data = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line_to_list = [letter for letter in line.strip("\n ")]
            all_data.append(line_to_list)

    return all_data


def create_character_locations(
    input_map: List[List[str]],
) -> Dict[str, List[Tuple[int, int]]]:
    """
    Finds all characters and adds it's string, and coordinates to a dict

    Args:
        input_map (List[List[str]]): The processed input data

    Returns:
        Dict[str, List[Tuple[int, int]]]:
            A dictionary where the characters are the keys,
            and the coordinates are the values
    """
    character_locations = {}

    for x, row in enumerate(input_map):
        for y, char in enumerate(row):
            if char != ".":
                if char not in character_locations:
                    character_locations[char] = []
                character_locations[char].append(
                    (y, x)  	# Accidentally swapped the x and y :)
                )

    return character_locations


def calculate(
    all_locations: Dict[str, List[Tuple[int, int]]],
    data: List[List[str]]
) -> Set[Tuple[int, int]]:
    """
    Calculates where all anti-nodes should be

    Args:
        all_locations (Dict[str, List[Tuple[int, int]]]):
        A dict with all characters as keys and its occurrences as values.

        data (List[List[str]]): The data in a nested list


    Returns:
        Set[Tuple[int, int]]:
            A set for non duplication with all locations of antinodes
    """
    all_antinodes = set()
    map_height = len(data)
    map_width = len(data[0])

    for _, coordinates in all_locations.items():
        for i, (x1, y1) in enumerate(coordinates):
            for j in range(i + 1, len(coordinates)):
                x2, y2 = coordinates[j]

                dx = x2 - x1
                dy = y2 - y1

                antinode1 = (x1 - dx, y1 - dy)
                antinode2 = (x2 + dx, y2 + dy)

                if (0 <= antinode1[0] < map_height
                        and 0 <= antinode1[1] < map_width):
                    all_antinodes.add(antinode1)

                if (0 <= antinode2[0] < map_height
                        and 0 <= antinode2[1] < map_width):
                    all_antinodes.add(antinode2)

    return all_antinodes


if __name__ == "__main__":
    data = read_data("2024/inputs/Assignment8_sample.txt")
    all_locations = create_character_locations(data)
    all_antinodes = calculate(all_locations, data)
