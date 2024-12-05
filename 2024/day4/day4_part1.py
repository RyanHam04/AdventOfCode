import numpy as np


def read_data(file_path: str) -> np.ndarray:
    """Used for reading the data into a format thats
    convenient for the assignment of day 4 into an numpy array.

    I chose a numpy array because it could easily be rotated 90 degrees.
    This is useful for reusability

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


def get_straight(data: np.ndarray) -> int:
    """
    Gets the total amount of straight lines, being vertical or horizontal
    depending on the orientation of the np.array,
    that contain either "XMAS" or its inverse

    Args:
        data (np.ndarray): The 2D array to check trough
        "XMAS"

    Returns:
        int: The total amount of "XMAS" occurrences
    """

    total = 0
    for line in data:
        stringed_line = ''.join(map(str, line))
        count = stringed_line.count("XMAS")
        count_inverse = stringed_line.count("SAMX")
        if count or count_inverse:
            total += count + count_inverse
    return total


def get_all_diagonals(data: np.ndarray) -> int:
    """
    Gets total amount of diagonals, being positive or negative lines
    depending on the orientation of the np.array,
    that contain either "XMAS" or its inverse
    Args:
        data (np.ndarray): The 2D array to look through

    Returns:
        total (int): The total amount of occurrences of "XMAS" in the diagonals
    """

    total = 0
    for offset in range(-data.shape[0] + 1, data.shape[1]):
        line = np.diagonal(data, offset=offset)

        stringed_line = ''.join(map(str, line))
        count = stringed_line.count("XMAS")
        count_inverse = stringed_line.count("SAMX")
        if count or count_inverse:
            total += count + count_inverse

    return total


if __name__ == "__main__":
    sample_data = read_data("2024/inputs/Assignment4_sample.txt")
    personal_data = read_data("2024/inputs/Assignment4_input.txt")

    rotated_data = np.rot90(personal_data)
    horizontal = get_straight(personal_data)
    vertical = get_straight(rotated_data)

    negative_diagonal = get_all_diagonals(personal_data)
    positive_diagonal = get_all_diagonals(rotated_data)
    final = horizontal + vertical + negative_diagonal + positive_diagonal
    print(final)
