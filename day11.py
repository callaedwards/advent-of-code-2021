from setup import get_input_file_path
from typing import List, Tuple
from collections import defaultdict

sample_data = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""


def main():
    input_file = get_input_file_path()
    with open(input_file) as f:
        lines = f.read().split("\n")
        c1 = None
        c2 = None
        print("part1:", c1, "\npart2:", c2)


if __name__ == "__main__":
    main()
