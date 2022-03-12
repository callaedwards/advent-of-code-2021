from setup import get_input_file_path
from typing import List, Dict, Tuple

sample_data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def calc_min_fuel(submarines: List[int]) -> int:
    min_position = min(submarines)
    max_position = max(submarines)

    min_fuel = None

    for i in range(min_position, max_position + 1):
        current_fuel = liner_fuel(submarines, i)
        if not min_fuel or current_fuel < min_fuel:
            min_fuel = current_fuel

    return min_fuel


def calc_min_fuel2(submarines: List[int]) -> int:
    min_position = min(submarines)
    max_position = max(submarines)

    min_fuel = None

    for i in range(min_position, max_position + 1):
        current_fuel = exponential_fuel(submarines, i)
        if not min_fuel or current_fuel < min_fuel:
            min_fuel = current_fuel

    return int(min_fuel)


def liner_fuel(submarines: List[int], position: int) -> int:
    current_fuel = 0
    for submarine in submarines:
        current_fuel += abs(submarine - position)

    return current_fuel


def exponential_fuel(submarines: List[int], position: int) -> int:
    current_fuel = 0
    for submarine in submarines:
        n = abs(submarine - position)
        current_fuel += (n+1) * (n/2)

    return current_fuel


def main():
    input_file = get_input_file_path()
    with open(input_file) as f:
        lines_input = f.read()

        parsed_input = [int(line) for line in lines_input.split(",")]

        c1 = calc_min_fuel(parsed_input)
        c2 = calc_min_fuel2(parsed_input)
        print("part1:", c1, "\npart2:", c2)


if __name__ == "__main__":
    main()
