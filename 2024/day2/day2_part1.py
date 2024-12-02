from typing import List


def read_data(file_path: str) -> List[List[int]]:
    """Used for reading the data into a format thats
    convenient for the assignment of day 2

    Args:
        file_path (str): The directory of the file containing the data (.txt)

    Returns:
        List[List[int]]: Nested list containing different "reports"
                        which contain values
    """
    all_data = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line_to_list = [int(num) for num in line.strip("\n ").split()]
            all_data.append(line_to_list)
    return all_data


def wrong_direction(left: int, right: int, increasing: bool) -> bool:
    """Checks if two values follow a relation
    This relation is calculated by safety_check and is the relation
    between the first and second value

    Args:
        left (int): Value at the left pointer of the report
        right (int): Value at the right pointer of the report
        increasing (bool): _description_

    Returns:
        bool: If the values dont follow
        the relation it returns True, else False
    """
    if left > right and increasing:
        return True
    if left < right and not increasing:
        return True
    return


def difference_check(left: int, right: int) -> bool:
    """Calculates two values have the right amount of difference

    Args:
        left (int): Value at the left pointer of the report
        right (int): Value at the right pointer of the report

    Returns:
        bool: Returns True if the difference is 1, 2 or 3
    """

    difference = abs(left - right)
    return difference > 3 or difference < 1


def safety_check(data: List[List[int]]) -> int:
    """Iterates over the reports by the use of pointers.
    It checks if all requirements are met and returns the
    total amount of reports that follow these requirements

    Args:
        data (List[List[int]]): Nested list containing the reports,
                                which contain different values

    Returns:
        int: The total amount of reports that meet the requirements
    """
    total = 0
    for report in data:
        left = 0
        right = 1
        increasing = True if report[left] < report[right] else False

        while True:
            if difference_check(report[left], report[right]):
                break
            if wrong_direction(report[left], report[right], increasing):
                break
            if right == len(report) - 1:
                total += 1
                break
            left += 1
            right += 1
    return total


if __name__ == "__main__":
    sample_data = read_data("2024/inputs/Assignment2_sample.txt")
    personal_data = read_data("2024/inputs/Assignment2_input.txt")
    print(safety_check(data=sample_data))
    print(safety_check(data=personal_data))
