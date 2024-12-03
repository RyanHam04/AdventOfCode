
import re
from typing import List, Tuple


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


def regex_finder(data: str) -> List[Tuple[str, str, str]]:
    """
    Returns a list with tuples with containing either:
        *do -> if do() found else ""
        *dont -> if don't() is found else ""
        *x,y -> if mul(x,y) found, it returns the inner values else ""

    Args:
        data (str): The data in which is being searched

    Returns:
        List[str, str, str]: do(), don't() and x,y
    """
    result = re.findall(r"(do\(\))|(don't\(\))|mul\(([0-9]+,[0-9]+)\)", data)

    return result


def sum_legal_multiplication(regex_result: List[Tuple[str, str, str]]) -> int:
    """Iterates over the regex result and
    adds to numbers inside the mul() string, if the
    most recent permission is true

    Args:
        result (List[Tuple[str, str, str]]): Contains either do, dont or values

    Returns:
        total (int): The total of the legal multiplications
    """
    total = 0
    permission = True

    for item in regex_result:
        do, dont, numbers = item
        if do:
            permission = True
        elif dont:
            permission = False
        else:
            num1, num2 = numbers.split(",")
            total += (int(num1) * int(num2)) if permission else 0

    return total


if __name__ == "__main__":
    data = read_data("2024/inputs/Assignment3_input.txt")
    result = regex_finder(data)

    total = sum_legal_multiplication(result)
    print(total)
