from setup import get_input_file_path
from typing import List



def find_most_common_bits(binary_readings: List[str]) -> str:
	column_sums = [0]*len(binary_readings[0])
	for binary in binary_readings:
		for i in range(len(binary)):
			column_sums[i] += int(binary[i])

	threshold = len(binary_readings) // 2

	binary_string = ""
	for col in column_sums:
		if col > threshold:
			binary_string += "1"
		else:
			binary_string += "0"
	return binary_string

def invert_bit_string(input_binary_string: str) -> str:
	output_binary_string = ""
	for bit in input_binary_string:
		if bit == "1":
			output_binary_string += "0"
		else:
			output_binary_string += "1"
	return output_binary_string

def binary_to_decimal(binary: str) -> int:
	return int(binary, 2)

def part1(binary_readings: List[str]) -> int:
	most_common_bits = find_most_common_bits(binary_readings)
	least_common_bits = invert_bit_string(most_common_bits)

	gamma_rate = binary_to_decimal(most_common_bits)
	epsilon_rate = binary_to_decimal(least_common_bits)

	power_consumption = gamma_rate * epsilon_rate
	return(power_consumption)


def find_most_common_bit(binary_readings: List[str], index: int) -> str:
	sum = 0
	for binary in binary_readings:
		sum += int(binary[index])

	threshold = len(binary_readings) / 2
	if sum >= threshold:
		return 1
	else:
		return 0


def find_least_common_bit(binary_readings: List[str], index: int) -> str:
	sum = 0
	for binary in binary_readings:
		sum += int(binary[index])

	threshold = len(binary_readings) / 2

	if sum >= threshold:
		return 0
	else:
		return 1


def find_match(binary_readings: List[str], most_common: bool) -> str:
	match = ""
	matches = binary_readings
	i = 0
	while(len(matches) > 1):
		if most_common:
			desired_bit = find_most_common_bit(matches, i)
		else:
			desired_bit = find_least_common_bit(matches, i)
		match += str(desired_bit)
		matches = [b for b in binary_readings if b.startswith(match)]
		i += 1
	return matches[0]


def part2(binary_readings: List[str]) -> int:
	most_common_bit_result = find_match(binary_readings, True)
	oxygen_generator_reating = binary_to_decimal(most_common_bit_result)

	least_common_bit_result = find_match(binary_readings, False)
	co2_scrubber_rating = binary_to_decimal(least_common_bit_result)

	life_support_rating = oxygen_generator_reating * co2_scrubber_rating

	return(life_support_rating)


def main():
	input_file = get_input_file_path()
	with open(input_file) as f:
		binary_readings = [line.strip() for line in f.readlines()]
		a1 = part1(binary_readings)
		a2 = part2(binary_readings)

	print(a1)
	print(a2)


if __name__ == "__main__":
    main()
