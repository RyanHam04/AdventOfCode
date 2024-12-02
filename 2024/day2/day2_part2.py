from day2_part1 import read_data, wrong_direction, difference_check
from typing import List


def legal(left: int, right: int, increasing: bool) -> bool:
    """Checks if the report is legal
    *Two adjacent numbers have to differ at least one point
    *Two adjacent numbers cannot be more than 3 points apart
    *The entire list has to be either increasing or decreasing in values

    Args:
        left (int): The value of the list at the left pointer
        right (int): The value of the list at the right pointer
        increasing (bool): The relationship between the first two numbers
                            True = Increasing, False = Decreasing

    Returns:
        bool: _description_
    """
    if difference_check(left, right):
        return False
    if wrong_direction(left, right, increasing):
        return False
    return True


def check_valid_version(report: List[int]) -> bool:
    """
    This function checks if there is any valid set in the report
    by skipping one of the items from the report
    It does this by, like safety_check, the use of pointers
    and creation of different copies of the report

    Args:
        report (List[int]): the report

    Returns:
        bool: Indicates whether there exists a valid version of the list
        with one allowed penalty
    """

    for i in range(len(report)):
        report_copy = report[:i] + report[i + 1:]
        left = 0
        right = 1
        increasing = True if report_copy[left] < report_copy[right] else False

        valid = True
        while right < len(report_copy):
            if not legal(report_copy[left], report_copy[right], increasing):
                valid = False
                break
            left += 1
            right += 1

        if valid:
            return True

    return False


def safety_check(data: List[List[int]]) -> int:
    """Counts the amount of legal reports from the data

    Args:
        data (List[List[int]]): A list containing all the reports

    Returns:
        int: The total amount of reports that fit the requirements
        with removal of one integer per report allowed.
    """
    total = 0
    for report in data:
        left = 0
        right = 1
        increasing = True if report[left] < report[right] else False
        penalty = False

        while True:
            if right == len(report):  # The list has been parsed
                total += 1
                print(report)
                break
            if legal(report[left], report[right], increasing):
                left += 1
                right += 1
                continue
            if not penalty:
                if check_valid_version(report):
                    penalty = True
                    total += 1
                break
    return total


if __name__ == "__main__":
    sample_data = read_data("2024/inputs/Assignment2_sample.txt")
    personal_data = read_data("2024/inputs/Assignment2_input.txt")

    print(safety_check(data=sample_data))
    print(safety_check(data=personal_data))
