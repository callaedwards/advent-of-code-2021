from setup import get_input_file_path
from typing import List

BOARD_SIZE = 5


def part1(bingo_boards: List[List[str]], numbers_called: List[str]) -> int:
	pass







def main():
	input_file = get_input_file_path()
	with open(input_file) as f:
		bingo_input = f.read().split("\n\n")
		numbers_called = bingo_input[0].split(",")

		board_raw = [board.split() for board in bingo_input[1:]]
		board_parsed = [board[b:b+BOARD_SIZE] for board in board_raw for b in range(0, len(board), BOARD_SIZE)]

		a1 = part1(board_parsed)
		# a2 = part2(binary_readings)

	print(a1)
	# print(a2)


if __name__ == "__main__":
    main()


# [[1,2,3,2,3,4,5,6,7],[[1,2,3],[2,3,4],[5,6,7]]]
# [[[1,2,3],[2,3,4],[5,6,7]],[[1,2,3],[2,3,4],[5,6,7]]]