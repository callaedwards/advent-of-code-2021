from setup import get_input_file_path
from typing import List


def find_most_common_bits(binaries: List[str]) -> str:
	ans = [0]*len(binaries[0])
	for binary in binaries:
		for i in range(len(binary)):
			ans[i] += int(binary[i])

	threshold = len(binaries) // 2
	b = ""
	for a in ans:
		if a > threshold:
			b += "1"
		else:
			b += "0"
	return b

def find_least_common_bits(binary: str) -> str:
	c = ""
	for b in binary:
		if b == "1":
			c += "0"
		else:
			c += "1"
	return c

def binary_to_decimal(binary: str) -> int:
	return int(binary, 2)


def main():
	input_file = get_input_file_path()
	with open(input_file) as f:
		binaries = [line.strip() for line in f.readlines()]
		f1 = find_most_common_bits(binaries)
		f2 = find_least_common_bits(f1)

	print(f1,f2)
	print(binary_to_decimal(f1) * binary_to_decimal(f2))
		#c2 = count_depth_window_increases(depths)
	#print("part1:", c1,"\npart2:", c2)

if __name__ == "__main__":
    main()