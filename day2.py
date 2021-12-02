from typing import List

def calculate_depth_and_position(lines: List[str]) -> int:
	depth = 0
	position = 0
	for line in lines:
		direction, value = line.split()
		value = int(value)
		if direction == "up":
			depth -= value
		elif direction == "down":
			depth += value
		elif direction == "forward":
			position += value
	return(position * depth)

def calculate_depth_and_position_with_aim(lines: List[str]) -> int:
	depth = 0
	position = 0
	aim = 0
	for line in lines:
		direction, value = line.split()
		value = int(value)
		if direction == "up":
			aim -= value
		elif direction == "down":
			aim += value
		elif direction == "forward":
			position += value
			depth += aim * value
	return(position * depth)

def main():
	with open('input2.txt') as f:
		lines = f.readlines()
		a1 = calculate_depth_and_position(lines)
		a2 = calculate_depth_and_position_with_aim(lines)
	print("part1:", a1,"\npart2:", a2)

if __name__ == "__main__":
    main()