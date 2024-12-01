from Day1_part1 import read_data
from typing import List


def similarity_analysis(left: List[int], right: List[int]) -> int:
    """
    Description:
        Iterates over the left list.
        If the key does not exist yet, then it will add it to the dict
        This so it only has to check the occurrences once.
    Args:
        left (List[int]): List containing Location ID's
        right (List[int]): List containing Location ID"s

    Returns:
        similarity_score (int): The sum of each item in the left list
        multiplied by the frequency of that same item in the right list
    """

    similarity_score = 0
    occurrences = {}
    for i in left:
        occurrences[i] = right.count(i)
        similarity_score += i * occurrences[i]
    return similarity_score


if __name__ == "__main__":
    left, right = read_data()
    print(
        similarity_analysis(  # AdventOfCode example input
            [3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]
        )
    )
    print(similarity_analysis(left, right))  # Personal data
