from setup import get_input_file_path
from typing import List, Dict, Tuple

sample_data = [3, 4, 3, 1, 2]


def count_fish(lantern_fish: List[int], days: int) -> int:
    # {days left => count of fish}
    days_left = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    for fish in lantern_fish:
        days_left[fish] += 1

    return some_days_later2(days_left, days)


def some_days_later2(days_left: Dict[int, int], days: int) -> int:
    for _ in range(days):
        temp = days_left[0]
        for i in range(8):
            days_left[i] = days_left[i+1]
        days_left[8] = temp
        days_left[6] += temp

    return sum_fish(days_left)


def sum_fish(days_left: Dict[int, int]) -> int:
    fish_sum = 0
    for day in days_left:
        fish_sum += days_left[day]
    return fish_sum


def main():
    input_file = get_input_file_path()
    with open(input_file) as f:
        lines_input = f.read()

        parsed_input = [int(line) for line in lines_input.split(",")]

        c1 = count_fish(parsed_input, 80)
        c2 = count_fish(parsed_input, 256)
        print("part1:", c1, "\npart2:", c2)


if __name__ == "__main__":
    main()
