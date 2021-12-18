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
		#axis[index].add(target_value * -1)


def part1(bingo_boards: List[List[List[str]]], numbers_called: List[str]) -> int:
	boards = []
	for bingo_board in bingo_boards:
		boards += [Board(bingo_board)]

	winning_board = None
	winning_move_count = len(numbers_called)
	for board in boards:
		move_count = check_win(board, numbers_called)
		if move_count < winning_move_count:
			winning_move_count = move_count
			winning_board = board

	total = 0
	for row in board.rows:
		while len(row) > 0:
			total += row.pop()

	#print(numbers_called)
	#print(len(numbers_called))
	#print(winning_move_count)
	multiplier = int(numbers_called[winning_move_count])
	print(total)
	print(multiplier)
	return total * multiplier


def check_win(board: Board, numbers_called: List[str]) -> int:
	i = 1
	is_done = False
	while i < len(numbers_called) and not is_done:
		# check_horizontals()
		for r in range(len(board.rows)):
			target_value = int(numbers_called[i])
			if target_value in board.rows[r]:
				board.mark(r, target_value, True)

		# check_verticals()
		for c in range(len(board.columns)):
			target_value = int(numbers_called[i])
			if target_value in board.rows[c]:
				board.mark(c, target_value, False)
		
		for j in range(len(board.rows)):
			if len(board.rows[r]) == 0 or len(board.columns[c]) == 0:
				is_done = True

		i += 1
	return i

# def check_horizontals():
# 	pass



def main():
	#input_file = get_input_file_path()
	input_file = "inputs/day4test.txt"
	with open(input_file) as f:
		bingo_input = f.read().split("\n\n")
		numbers_called = bingo_input[0].split(",")

		parsed_boards = [board.split() for board in bingo_input[1:]]
		for i in range(len(parsed_boards)):
			parsed_boards[i] = [parsed_boards[i][b:b+BOARD_SIZE] for b in range(0, len(parsed_boards[i]), BOARD_SIZE)]

		a1 = part1(parsed_boards, numbers_called)
		# a2 = part2(binary_readings)
	
	print(a1)
	# print(a2)


if __name__ == "__main__":
    main()



