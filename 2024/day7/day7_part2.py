from day7_part1 import TreeNode, read_data, find_leaf_paths
from typing import List


def build_tree(numbers: List[int]) -> TreeNode:
    """
    Same method as in part 1 except added "||" as operator
    This operator acts as a append function, it adds the following number
    to the current total at the parent node.

    Args:
        numbers (List[int]): The numbers included for the operation

    Returns:
        TreeNode: Node in the tree, which is one of the numbers
    """

    root = TreeNode(0, None)

    current_level = [root]

    for number in numbers:
        next_level = []
        for node in current_level:
            plus_child = TreeNode(node.number + number, f"+{number}")
            node.add_child(plus_child)
            next_level.append(plus_child)

            multiply_child = TreeNode(node.number * number, f"*{number}")
            node.add_child(multiply_child)
            next_level.append(multiply_child)

            concat_child = TreeNode(int(str(node.number) + str(number)),
                                    f"||{number}")
            node.add_child(concat_child)
            next_level.append(concat_child)
        current_level = next_level

    return root


def main() -> None:
    """
    Main logic for calculating the total:
        -Reads data
        -Iterates and builds the tree for each line in the data
        -Checks if there are paths which total to the goal
        -Adds the goal to total if there is a solution
        -Prints the total
    """
    goals, number_list = read_data("2024/inputs/Assignment7_input.txt")
    total = 0
    for idx, numbers in enumerate(number_list):
        root = build_tree(numbers)
        if find_leaf_paths(root, goals[idx]):
            total += goals[idx]

    print(total)


if __name__ == "__main__":
    main()
