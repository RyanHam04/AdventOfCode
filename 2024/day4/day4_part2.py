import numpy as np
import re
from day4_part1 import read_data

# NE, NW, SW, SE respectively
DIRECTIONS = [(-1, -1), (-1, 1), (1, 1), (1, -1)]


def mask(data: np.ndarray, value: str) -> np.ndarray:
    """Returns boolean mask which consists of
    True for values in data == value
    False for values in data != value


    Args:
        data (np.ndarray): Data containing the input data as a 2D array
        value (str): The value you want to check in the data,
                    in day 4 of AoC, this is "A"

    Returns:
        mask (np.ndarray): The boolean mask
    """
    return data == value


def pad(data: np.ndarray) -> np.ndarray:
    """
    Creates a ring of empty strings around the original array
    This is to prevent Index and other errors

    Args:
        data (np.ndarray): Data in a 2D array

    Returns:
        np.ndarray: Data with a ring of empty strings
    """
    return np.pad(data,
                  pad_width=1,
                  mode='constant',
                  constant_values="")


def shift_array(padded_data: np.ndarray, data: np.ndarray) -> np.ndarray:
    """
    Gets the corners of the "A" values.

    Args:
        padded_data (np.ndarray): 2D array with a ring of ""
        data (np.ndarray): 2D array with the original data

    Returns:
        corenrs (np.ndarray): 2D array with the corners of the "A" values.
    """
    corners = None
    for row_offset, col_offset in DIRECTIONS:
        shifted = padded_data[1 + row_offset: 1 + row_offset + data.shape[0],
                              1 + col_offset: 1 + col_offset + data.shape[1]]

        try:
            corners = np.char.add(corners, shifted)
        except (TypeError, NameError):
            corners = shifted

    return corners


def count_matches(corners, mask) -> int:
    """
    Uses regex to check if the corners of A have the M and S values correct

    Args:
        corners (np.ndarray): The corners of the "A" values
        mask (np.ndarray): The boolean mask,
                           to check where there are "A" values quickly

    Returns:
        count (int): The occurrences where there
            is an MAS or SAM in both diagonals
    """
    count = 0
    for corner in corners[mask]:
        if re.match(r"(SSMM|SMMS|MMSS|MSSM)", corner):
            count += 1
    return count


if __name__ == "__main__":

    data = read_data("2024/inputs/Assignment4_input.txt")
    padded_data = pad(data)
    mask = mask(data, "A")
    corners = shift_array(padded_data, data)
    count = count_matches(corners, mask)

    print(count)
