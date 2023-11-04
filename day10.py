from setup import get_input_file_path
from typing import List, Tuple
from collections import defaultdict

sample_data = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

OPEN_CHUNK = frozenset(["(", "[", "{", "<"])
CHUNK_MAP = {")": "(", "]": "[", "}": "{", ">": "<"}
INCOMPLETE_SCORE = {"(": 1, "[": 2, "{": 3, "<": 4}


def find_corrupted(data: List[str]) -> Tuple[int, List[str]]:
    counter = defaultdict(int)
    incomplete = []
    for line in data:
        stack = []
        for c in line:
            if c in OPEN_CHUNK:
                stack.append(c)
            elif stack[-1] == CHUNK_MAP[c]:
                stack.pop()
            else:
                counter[c] += 1
                stack = []
                break
        if len(stack) != 0:
            incomplete.append(line)
    score = counter[")"] * 3 + counter["]"] * 57 + counter["}"] * 1197 + counter[">"] * 25137
    return score, incomplete


def find_incomplete(data: List[str]) -> int:
    scores = []
    for line in data:
        score = 0
        stack = []
        for c in line:
            if c in OPEN_CHUNK:
                stack.append(c)
            elif stack[-1] == CHUNK_MAP[c]:
                stack.pop()

        while len(stack) > 0:
            chunk = stack.pop()
            score = (score * 5) + INCOMPLETE_SCORE[chunk]
        scores.append(score)

    scores.sort()
    return scores[len(scores) // 2]


def main():
    input_file = get_input_file_path()
    with open(input_file) as f:
        lines = f.read().split("\n")
        c1, lines = find_corrupted(lines)
        c2 = find_incomplete(lines)
        print("part1:", c1, "\npart2:", c2)


if __name__ == "__main__":
    main()
