from typing import List

# NOTE I know this code is very slow and likely suboptimal
# However, it reached the solution in less than a minute which is fine by me for now
# I just want to catch up :) Optimizing is for another day
# TODO STYLING


def read_data(file_path: str) -> List[str]:

    all_data = []
    with open(file_path, "r", encoding="utf-8") as f:
        for char in f.read():
            all_data.append(char)

    return all_data


def process_data(data):
    result = []
    block = True  # If false, then free space
    count = 0
    for char in data:
        if block:
            result.extend([str(count)] * int(char))
            count += 1
            block = False
        else:
            result.extend(["."] * int(char))
            block = True
    return result


def update_file(data, dot_index):
    for num_index in range(1, len(data) - dot_index):
        if data[-num_index].isnumeric():
            data[dot_index] = data[-num_index]
            data[-num_index] = "."
            break
    return data


def filecompact(data):
    count = 0
    result = list(data)
    for idx, char in enumerate(result):
        if char == "." and any(item.isnumeric() for item in result[idx:]):
            update_file(result, idx)

            count += 1
    return result, count


def calculate_checksum(formatted):
    total = 0
    for idx, char in enumerate(formatted):
        if char == ".":
            return total

        total += (idx * int(char))

    return total


if __name__ == "__main__":
    data = read_data("2024/inputs/Assignment9_input.txt")
    data = process_data(data)
    formatted, count = filecompact(data)
    print(calculate_checksum(formatted))
