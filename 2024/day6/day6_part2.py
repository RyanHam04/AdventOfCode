import numpy as np
from day6_part1 import read_data, pad, find_start, modify_coordinates


def calculate_route(data: np.ndarray, x: int, y: int,
                    orientation: int, visited_states: set) -> bool:
    """
    Calculates the route of the guard and detects
    if the patrol results in an infinite loop.

    Args:
        data (np.ndarray): The map of the guard's field
        x (int): Current x-coordinate
        y (int): Current y-coordinate
        orientation (int): Initial direction (0-3 for up/right/down/left)
        visited_states (set): Set to track visited states

    Returns:
        bool: True if an infinite loop is detected, False otherwise
    """
    while True:
        current_state = (x, y, orientation)
        if current_state in visited_states:
            return True

        visited_states.add(current_state)

        new_x, new_y = modify_coordinates(x, y, orientation)
        if data[new_y][new_x] == "#":
            orientation = (orientation + 1) % 4
        elif data[new_y][new_x] == "":
            return False
        else:
            x, y = new_x, new_y


def count_infinite_loops(data: np.ndarray, start_x: int, start_y: int) -> int:
    """
    Counts the number of new obstacles that generate
    infinite loops in the guard's patrol.

    Args:
        data (np.ndarray): The map of the guard's field
        start_x (int): Starting x-coordinate of the guard
        start_y (int): Starting y-coordinate of the guard

    Returns:
        int: The number of obstacles that generate infinite loops
    """
    infinite_loop_count = 0

    for y in range(1, data.shape[0] - 1):
        for x in range(1, data.shape[1] - 1):
            if data[y][x] not in {"#", ""}:
                modified_data = data.copy()
                modified_data[y][x] = "#"

                visited_states = set()
                if calculate_route(
                    modified_data, start_x, start_y, orientation=0,
                    visited_states=visited_states
                ):
                    infinite_loop_count += 1

    return infinite_loop_count


if __name__ == "__main__":
    data = read_data("2024/inputs/Assignment6_input.txt")
    padded_data = pad(data)
    start_y, start_x = find_start(padded_data)

    infinite_loops = count_infinite_loops(padded_data, start_x, start_y)

    print(f"Infinite loops: {infinite_loops}")
