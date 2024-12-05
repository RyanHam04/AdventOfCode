from typing import List, Tuple


def read_data(file_path: str) -> Tuple[List[Tuple[int, int]], List[List[int]]]:
    """
    Returns the data in the most convenient structure.

    Args:
        file_path (str): The directory of the file to be read

    Returns:
        rules: List[Tuple[int, int]]: split by "|" in the original file
        updates: List[List[int]]: split by "," in the original file

    """

    rules = []
    updates = []

    with open(file_path, "r", encoding="utf-8") as f:
        raw_rules, raw_updates = f.read().strip().split("\n\n")
        for line in raw_rules.splitlines():
            rules.append(list(map(int, line.split("|"))))
        for line in raw_updates.splitlines():
            updates.append(list(map(int, line.split(","))))

    return rules, updates


def is_update_valid(update: List[int], rules: List[Tuple[int, int]]) -> bool:
    """
    Checks for each rule if the first value
    in that rule is behind the second value in the new update

    Args:
        update (List[int]): The update to be checked
        rules (List[Tuple[int, int]]): The restrictions for updates

    Returns:
        bool: False if the rule is not met, True if all rules have been checked
    """

    for first, second in rules:
        if first in update and second in update:
            if update.index(first) > update.index(second):
                return False
    return True


def find_middle(update: List[int]) -> int:
    """Helper function for getting the middle value of the update list

    Args:
        update (List[int]): The updates that are correct

    Returns:
        int: The middle value of the correct updates
    """

    return update[len(update) // 2]


def process_updates(rules: List[Tuple[int, int]],
                    updates: List[List[int]]) -> int:
    """
    Main logic, checks restrictions for all updates and
    adds their middle value to the total count if true.

    Args:
        rules (List[Tuple[int, int]]): The restriction rules
        updates (List[List[int]]): The updates

    Returns:
        int: Total of all middle values of the valid updates
    """
    total = 0

    for update in updates:
        if is_update_valid(update, rules):
            total += find_middle(update)

    return total


if __name__ == "__main__":
    rules, updates = read_data("2024/inputs/Assignment5_sample.txt")
    result = process_updates(rules, updates)
    print(result)
