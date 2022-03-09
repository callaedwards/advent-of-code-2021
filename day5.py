from setup import get_input_file_path
from typing import List, Dict, Tuple

sample_data = [
                "0,9 -> 5,9",
                "8,0 -> 0,8",
                "9,4 -> 3,4",
                "2,2 -> 2,1",
                "7,0 -> 7,4",
                "6,4 -> 2,0",
                "0,9 -> 2,9",
                "3,4 -> 1,4",
                "0,0 -> 8,8",
                "5,5 -> 8,2"
            ]


class Line:
    def __init__(self, line: List[str]):
        start, end = line
        self.start = Point.from_string(start)
        self.end = Point.from_string(end)

    def __str__(self) -> str:
        return "{" + str(self.start) + ", " + str(self.end) + "}"


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @classmethod
    def from_string(cls, coordinates: str):
        x, y = coordinates.split(",")
        x = int(x)
        y = int(y)
        return cls(int(x), int(y))

    def __str__(self) -> str:
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def create_lines(lines: List[List[str]]) -> List[Line]:
    return [Line(line) for line in lines]


def is_valid(line: Line) -> bool:
    if line.start.x == line.end.x or line.start.y == line.end.y:
        return True
    return False


def find_intersections(lines: List[Line], include_diagonals=False):
    point_dict = {}
    for line in lines:
        points = get_points(line, include_diagonals)
        for point in points:
            tupled_point = (point.x, point.y)
            if tupled_point in point_dict:
                point_dict[tupled_point] += 1
            else:
                point_dict[tupled_point] = 1

    return count_intersections(point_dict)


def get_points(line: Line, include_diagonals: bool) -> List[Point]:
    points = []
    if line.start.x == line.end.x:
        lower_y_bound = min(line.start.y, line.end.y)
        upper_y_bound = max(line.start.y, line.end.y)
        for y in range(lower_y_bound, upper_y_bound + 1):
            points.append(Point(line.start.x, y))

    elif line.start.y == line.end.y:
        lower_x_bound = min(line.start.x, line.end.x)
        upper_x_bound = max(line.start.x, line.end.x)
        for x in range(lower_x_bound, upper_x_bound + 1):
            points.append(Point(x, line.start.y))

    elif include_diagonals and abs(line.start.x-line.end.x) == abs(line.start.y-line.end.y):
        x_inc = 1 if line.start.x < line.end.x else -1
        y_inc = 1 if line.start.y < line.end.y else -1

        x = line.start.x
        y = line.start.y
        while x != line.end.x and y != line.end.y:
            points.append(Point(x, y))
            x += x_inc
            y += y_inc
        points.append(Point(x, y))
    return points


def count_intersections(points: Dict[Tuple[int, int], int]) -> int:
    count = 0
    for point in points:
        if points[point] >= 2:
            count += 1

    return count


def main():
    input_file = get_input_file_path()
    with open(input_file) as f:
        lines_input = f.readlines()

        parsed_lines = [line.strip().split(" -> ") for line in lines_input]
        lines = create_lines(parsed_lines)

        c1 = find_intersections(lines)
        c2 = find_intersections(lines, True)
        print("part1:", c1, "\npart2:", c2)


if __name__ == "__main__":
    main()
