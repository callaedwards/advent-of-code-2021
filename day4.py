from setup import get_input_file_path
from typing import List, Tuple

BOARD_SIZE = 5


class Board:
	def __init__(self, board: List[List[str]]):
		rows = []
		columns = []
		for i in range(len(board)):
			column_list = [int(r[i]) for r in board]
			row_list = [int(board[i][j]) for j in range(len(board))]

			columns += [set(column_list)]
			rows += [set(row_list)]

		self.rows = rows
		self.columns = columns

	def __str__(self) -> str:
		return str({"rows": self.rows,"columns": self.columns})

	def mark(self, index: int, target_value: int, is_row: bool):
		if is_row:
			self.rows[index].remove(target_value)
		else:
			self.columns[index].remove(target_value)


def part1(bingo_boards: List[List[List[str]]], numbers_called: List[int]) -> int:
	boards = create_boards(bingo_boards)

	winning_board = None
	winning_move_index = len(numbers_called)
	
	for board in boards:
		print(board)
		move_index = find_win_index(board, numbers_called)
		if move_index < winning_move_index:
			winning_move_index = move_index
			winning_board = board

	total = 0
	for row in winning_board.rows:
		while len(row) > 0:
			total += row.pop()

	multiplier = numbers_called[winning_move_index]
	return total * multiplier


def create_boards(bingo_boards: List[List[List[str]]]) -> List[Board]:
	return [Board(bingo_board) for bingo_board in bingo_boards]


def find_win_index(board: Board, numbers_called: List[int]) -> int:
	for i in range(len(numbers_called)):
		target_value = numbers_called[i]

		# check_horizontals()
		for r in range(len(board.rows)):
			if target_value in board.rows[r]:
				board.mark(r, target_value, True)
				break

		# check_verticals()
		for c in range(len(board.columns)):
			if target_value in board.columns[c]:
				board.mark(c, target_value, False)
				break
		
		for row in board.rows:
			if len(row) == 0:
				return i

		for column in board.columns:
			if len(column) == 0:
				return i

	return i + 1


def main():
	input_file = get_input_file_path()
	with open(input_file) as f:
		bingo_input = f.read().split("\n\n")
		numbers_called = bingo_input[0].split(",")
		parsed_numbers_called = [int(num) for num in numbers_called]

		parsed_boards = [board.split() for board in bingo_input[1:]]
		for i in range(len(parsed_boards)):
			parsed_boards[i] = [parsed_boards[i][b:b+BOARD_SIZE] for b in range(0, len(parsed_boards[i]), BOARD_SIZE)]

		a1 = part1(parsed_boards, parsed_numbers_called)
		# a2 = part2(binary_readings)
	
	print(a1)
	# print(a2)


if __name__ == "__main__":
	main()




