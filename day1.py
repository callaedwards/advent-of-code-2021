
count = 0

with open('input.txt') as f:
	lines = f.readlines()
	curr = int(lines[0])
	for line in lines[1:]:
		if curr < int(line):
			count += 1
		curr = int(line)

print(count)