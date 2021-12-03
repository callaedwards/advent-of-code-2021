from setup import get_input_file_path
from typing import List


def count_depth_increases(depths: List[int]) -> int:
	count = 0
	prev_depth = depths[0]
	for depth in depths[1:]:
		if prev_depth < depth:
			count += 1
		prev_depth = depth
	return count

def count_depth_window_increases(depths: List[int]) -> int:
	count = 0
	v1 = depths[1]
	v2 = depths[2]
	prev_sum = depths[0] + v1 + v2

	for depth in depths[3:]:
		curr_sum = v1 + v2 + depth
		if prev_sum < curr_sum:
			count += 1
		prev_sum = curr_sum
		v1 = v2
		v2 = depth
	return count

def main():
	input_file = get_input_file_path()
	with open(input_file) as f:
		depths = [int(line) for line in f.readlines()]
		c1 = count_depth_increases(depths)
		c2 = count_depth_window_increases(depths)
	print("part1:", c1,"\npart2:", c2)

if __name__ == "__main__":
    main()