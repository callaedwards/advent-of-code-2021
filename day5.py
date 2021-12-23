from setup import get_input_file_path
from typing import List

coordinate_plane = {}


class Line:
    def __init__(self, line: List[str]):

        start, end = line
        self.start = Point(start)
        self.end = Point(end)

    def __str__(self) -> str:
        return "{" + str(self.start) + ", " + str(self.end) + "}"


class Point:
    def __init__(self, coordinates: str):
        x, y = coordinates.split(",")
        self.x = int(x)
        self.y = int(y)

    def __str__(self) -> str:
        return "(" + str(self.x) + ", " + str(self.y) + ")"


def create_lines(lines: List[List[str]]) -> List[Line]:
    return [Line(line) for line in lines if is_valid(line)]


def is_valid(line: Line) -> bool:
    if line.start.x == line.end.x or line.start.y == line.end.y:
        return True
    return False


def count_intersections(line1: Line, line2: Line) -> int:
    pass
    #if line1.start.x == line2.end.x:

    # else line.start.y == line.end.y:

    # 1. [3, 6], [5, 6]
    # 2. [3, 2], [3, 8]
    # 3. [4, 6], [6, 6]
    # 1 & 2 -> 1: [3,6]
    # 1 & 3 -> 2: [4, 6], [5, 6]


def find_intersections(lines: List[Line]):
    for j in range(len(lines)):
        for k in range(j+1, len(lines)):
            count_intersections(lines[j], lines[k])




def main():
    input_file = get_input_file_path()
    with open(input_file) as f:
        lines_input = f.readlines()

        parsed_lines = [line.strip().split(" -> ") for line in lines_input]
        lines = create_lines(parsed_lines)
        for line in lines:
            print(line)

        find_intersections(lines)


if __name__ == "__main__":
    main()
