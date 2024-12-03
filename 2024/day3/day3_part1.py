
import re
from typing import List


def read_data(file_path: str) -> str:
    """Used for reading the data into a format thats
    convenient for the assignment of day 3

    Args:
        file_path (str): The directory of the file containing the data (.txt)

    Returns:
        str: The entire string from the file, no further processing needed.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def regex_finder(data: str) -> List[str]:
    """Uses regex to find all valid mul(x,y)
    occurrences and returns them in a list.

    Args:
        data (str): the raw data on which it performs regex

    Returns:
        List[str]: List containing the valid x,y as an item in the list.
    """
    result = re.findall(r"mul\(([0-9]+,[0-9]+)\)", data)
    return result


def sum_multiplication(regex_result: List[str]) -> int:
    """
    Separates each item into an X and Y and multiplies them.
    Afterwards the get added to the total.

    Args:
        regex_result (List[str]): results from regex_finder,
        each item follows the "x,y" structure

    Returns:
        total (int): The sum of all multiplied items
    """

    total = 0

    for item in regex_result:
        num1, num2 = item.split(",")
        total += (int(num1) * int(num2))

    return total


if __name__ == "__main__":
    data = read_data("2024/inputs/Assignment3_input.txt")
    regex_result = regex_finder(data)
    total = sum_multiplication(regex_result)
