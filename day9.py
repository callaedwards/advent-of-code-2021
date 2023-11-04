from setup import get_input_file_path
from typing import List, Tuple

sample_data = """
2199943210
3987894921
9856789892
8767896789
9899965678
"""


def find_lowest(data: List[str]):
    levels = []
    for r in range(len(data)):
        for c in range(len(data[0])):
            digit = int(data[r][c])
            if r - 1 >= 0:
                if digit >= int(data[r-1][c]):
                    continue
            if r + 1 < len(data):
                if digit >= int(data[r+1][c]):
                    continue
            if c - 1 >=0:
                if digit >= int(data[r][c-1]):
                    continue
            if c + 1 < len(data[0]):
                if digit >= int(data[r][c+1]):
                    continue
            levels.append(digit)
    return levels


def find_lowest_coordinates(data: List[str]):
    coordinates = []
    for r in range(len(data)):
        for c in range(len(data[0])):
            digit = int(data[r][c])
            if r - 1 >= 0:
                if digit >= int(data[r-1][c]):
                    continue
            if r + 1 < len(data):
                if digit >= int(data[r+1][c]):
                    continue
            if c - 1 >=0:
                if digit >= int(data[r][c-1]):
                    continue
            if c + 1 < len(data[0]):
                if digit >= int(data[r][c+1]):
                    continue
            coordinates.append((r,c))
    return coordinates


def calculate_risk(levels: List):
    return sum(levels) + len(levels)


def find_largest_basins(data: List[str]):
    coords = find_lowest_coordinates(data)
    basins = [0, 0, 0]
    for coord in coords:
        basin = calculate_basin_size(coord, data)
        if basin > basins[0]:
            basins[1] = basins[0]
            basins[2] = basins[1]
            basins[0] = basin
        elif basin > basins[1]:
            basins[2] = basins[1]
            basins[1] = basin
        elif basin > basins[2]:
            basins[2] = basin

    return basins[0] * basins[1] * basins[2]


def calculate_basin_size(coord: Tuple[int], data: List[str]):
    visited = set()
    basin = set()
    r, c = coord

    while True:
        if r - 1 >= 0 and int(data[r - 1][c]) != 9:
            if (r - 1, c) not in basin and (r - 1, c) not in visited:
                basin.add((r - 1, c))
        if r + 1 < len(data) and int(data[r + 1][c]) != 9:
            if (r + 1, c) not in basin and (r + 1, c) not in visited:
                basin.add((r + 1, c))
        if c - 1 >= 0 and int(data[r][c - 1]) != 9:
            if (r, c - 1) not in basin and (r, c - 1) not in visited:
                basin.add((r, c - 1))
        if c + 1 < len(data[0]) and int(data[r][c + 1]) != 9:
            if (r, c + 1) not in basin and (r, c + 1) not in visited:
                basin.add((r, c + 1))
        visited.add((r, c))

        if len(basin) == 0:
            break
        r, c = basin.pop()

    return len(visited)


def main():
    input_file = get_input_file_path()
    with open(input_file) as f:
        lines = f.read().split("\n")
        c1 = calculate_risk(find_lowest(lines))
        c2 = find_largest_basins(lines)
        print("part1:", c1, "\npart2:", c2)


if __name__ == "__main__":
    main()
