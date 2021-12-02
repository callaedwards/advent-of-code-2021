from typing import List

def calculate_depth_and_position(instructions: List[str]) -> int:
	depth, position = 0
	
	for line in instructions:
		direction, value = line
		value = int(value)
		if direction == "up":
			depth -= value
		elif direction == "down":
			depth += value
		elif direction == "forward":
			position += value
	return(position * depth)

def calculate_depth_and_position_with_aim(instructions: List[str]) -> int:
	depth, position, aim = 0

	for line in instructions:
		direction, value = line
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
		instructions = [line.split() for line in f.readlines()]
		a1 = calculate_depth_and_position(instructions)
		a2 = calculate_depth_and_position_with_aim(instructions)
	print("part1:", a1,"\npart2:", a2)

if __name__ == "__main__":
    main()