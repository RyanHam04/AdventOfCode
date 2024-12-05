from day5_part1 import read_data, find_middle
from typing import List, Tuple


def is_update_invalid(update: List[int],
                      rules: List[Tuple[int, int]]) -> List[int] | None:
    """
    Checks if an update set is invalid with the rule-set,
    then swaps the values, and checks again. After the method
    swapped all values to fit the rules, the new update is returned

    Args:
        update (List[int]): An update to be checked
        rules (List[Tuple[int, int]]): The list of restrictions

    Returns:
        List[int] | None: New update with swapped values,
                            or None if the update was initially correct
    """

    for first, second in rules:
        if first in update and second in update:
            if update.index(first) > update.index(second):
                index_first = update.index(first)
                index_second = update.index(second)
                update[index_first] = second
                update[index_second] = first
                is_update_invalid(update, rules)
                return update
    return None


if __name__ == "__main__":
    rules, updates = read_data("2024/inputs/Assignment5_input.txt")
    total = 0
    for update in updates:
        new_update = is_update_invalid(update, rules)
        if new_update:
            total += find_middle(update)

    print(total)
