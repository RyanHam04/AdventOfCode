from typing import Tuple, List


def read_data(file_path: str) -> Tuple[List[int], List[List[int]]]:
    """
    Read and parse the data file.
    Args:
        file_path (str): The path to the file to be read.
    Returns:
        List[Tuple[int, List[int]]]: Parsed data where each rule is a tuple.
    """

    number_list = []
    goals = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                goal, numbers = line.strip().split(": ")
                goal = int(goal)
                number = list(map(int, numbers.split(" ")))
                goals.append(goal)
                number_list.append(number)
    return goals, number_list


class TreeNode:
    """
    Class representing nodes in a tree

    Attributes:
        number (int): current value of this node
        operator (str): "+" or "*"
        children (List[TreeNode]): Each node has children
    """
    def __init__(self, number: int, operator: str) -> None:
        self.number = number
        self.operator = operator
        self.children = []

    def add_child(self, child: "TreeNode") -> None:
        self.children.append(child)


def build_tree(numbers: List[int]) -> "TreeNode":
    """
    Builds the tree, adds for each number a node with
    the "+" and "*" operators, and does that operation
    on the total of its parent value.

    Creates a new TreeNode after operation


    Args:
        numbers (List[int]): _description_

    Returns:
        TreeNode: _description_
    """

    # Highly inefficient, half of the tree is 0's because:
    # The root is 0 and since both * and + are nodes, half is useless
    # Will update after pushing
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
        current_level = next_level

    return root


def find_leaf_paths(node: TreeNode, goal: int, path=None) -> bool:
    """
    Recursively searches for paths in the tree that results in the target

    Args:
        node (TreeNode): The current Node
        goal (int): goal or target value the method looks for in the tree
        path (_type_, optional): List of operations performed that
        reached the current value. Defaults to None.

    Returns:
        bool: True if there exists a path leading to the goal value
    """

    if path is None:
        path = []

    if node.operator:
        path.append(node.operator)

    if not node.children:
        if node.number == goal:
            return True
    else:
        return any(find_leaf_paths(child, goal, path.copy())
                   for child in node.children)


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
