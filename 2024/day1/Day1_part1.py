from typing import List, Union


def get_difference(left: List[int], right: List[int]) -> int:
    """My answer for Day 1 Of the Advent of Code

    Description:
        Gets the sum of differences of each item in two sorted arrays
    Args:
        left (list): left list
        right (list): right list
    """
    left = sorted(left)
    right = sorted(right)
    return sum([abs(left[i] - right[i]) for i in range(len(left))])


def read_data(file_path: str) -> Union[List[int], List[int]]:
    """
    Reads data from .txt file when copied and pasted directly from
    the AdventOfCode assignment

    Args:
        file_path (str): Directory of the file

    Returns:
        Union[List[int], List[int]]: The left and the right list of ID's
    """
    right_list = []
    left_list = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            left, right = map(int, line.strip("\n").split())
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list


if __name__ == "__main__":
    left_list, right_list = read_data()
    print(get_difference(left_list, right_list))
