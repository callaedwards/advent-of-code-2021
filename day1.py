from typing import List

def count_value_increases(lines: List[str]) -> int:
	count = 0
	prev_value = int(lines[0])
	for line in lines[1:]:
		if prev_value < int(line):
			count += 1
		prev_value = int(line)
	return count

def count_window_increases(lines: List[str]) -> int:
	count = 0
	v1 = int(lines[1])
	v2 = int(lines[2])
	prev_sum = int(lines[0]) + v1 + v2

	for line in lines[3:]:
		curr_sum = v1 + v2 + int(line)
		if prev_sum < curr_sum:
			count += 1
		prev_sum = curr_sum
		v1 = v2
		v2 = int(line)
	return count

def main():
	with open('input1.txt') as f:
		lines = f.readlines()
		c1 = count_value_increases(lines)
		c2 = count_window_increases(lines)
	print("part1:", c1,"\npart2:", c2)

if __name__ == "__main__":
    main()