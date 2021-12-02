
count = 0

with open('input.txt') as f:
	lines = f.readlines()
	v1 = int(lines[1])
	v2 = int(lines[2])
	prev = int(lines[0]) + v1 + v2

	for line in lines[3:]:
		sum = v1 + v2 + int(line)
		if prev < sum:
			count += 1
		prev = sum
		v1 = v2
		v2 = int(line)

print(count)