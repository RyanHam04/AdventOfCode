import numpy as np
from typing import Tuple


# Changes in coordinates for: Up, right, down, left respectively
ORIENTATIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def read_data(file_path: str) -> np.ndarray:
    """Used for reading the data into a format thats
    convenient for the assignment of day 6 into an numpy array.

    I chose a numpy array because it allows for easy manipulation of the data,
    such as quick indexing, slicing, and mathematical operations on the data.
    Additionally, numpy arrays are highly efficient for large datasets and make
    it easier to perform operations like padding, transformations, or counting,
    which are essential for this task.


    Args:
        file_path (str): The directory of the file containing the data (.txt)

    Returns:
        np.ndarray: The original data converted to a numpy 2D array
    """

    all_data = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line_to_list = [letter for letter in line.strip("\n ")]
            all_data.append(line_to_list)
    np_array = np.array(all_data)
    return np_array


def pad(data: np.ndarray) -> np.ndarray:
    """
    Creates a ring of empty strings around the original array
    This is to prevent Index and other errors

    Args:
        data (np.ndarray): Data in a 2D array

    Returns:
        np.ndarray: Data with a ring of empty strings
    """
    return np.pad(data, pad_width=1, mode="constant", constant_values="")


def find_start(data: np.ndarray) -> Tuple[int, int]:
    """Uses a numpy method to find the guard's starting position

    Args:
        data (np.ndarray): The data as a numpy array after padding

    Returns:
        Tuple[int, int]: The indexes/coordinates of the guard
    """
    y, x = np.where(data == "^")
    return y[0], x[0]


def modify_coordinates(x: int, y: int, orientation: int) -> Tuple[int, int]:
    """Modifies the coordinates to move in a direction

    Args:
        x (int): current X-coordinate
        y (int): current Y-coordinate
        orientation (int): Number 0-4 to indicate the direction

    Returns:
        Tuple[int, int]: The coordinates after moving the guard
    """
    dx, dy = ORIENTATIONS[orientation]
    x += dx
    y += dy
    return x, y


def calculate_route(
    data: np.ndarray, x: int, y: int, orientation: int, count: int
) -> int:
    """
    Calculates the route a guard patrols,
    every time an obstacle is encountered (Indicated by #),
    the guard should turn 90 degrees and walk straightforward

    Args:
        data (np.ndarray): The map of the guard's field
        x (int): Current x-coordinate
        y (int): Current y-coordinate
        orientation (int): Value indicating whether
                            the guard should move up/right/down/left
        count (int): Count indicating the unique cells visited by the guard

    Returns:
        count (int): The total number of unique cells the guard
        visits during patrol
    """

    new_x, new_y = modify_coordinates(x, y, orientation)
    while data[new_y][new_x] != "#":
        if data[new_y][new_x] == "":
            print("OOB ERROR")
            return len(np.where(data == "X")[0]) + 1
        elif data[y][x] != "X":
            count += 1
        data[y][x] = "X"
        x = new_x
        y = new_y
        data[y][x] = "^"

        new_x, new_y = modify_coordinates(x, y, orientation)

    next_orientation = (orientation + 1) % 4
    return calculate_route(data, x, y, next_orientation, count)


if __name__ == "__main__":

    data = read_data("2024/inputs/Assignment6_input.txt")
    padded = pad(data)
    y, x = find_start(padded)

    total = calculate_route(padded, x, y, orientation=0, count=0)
    print(total)
