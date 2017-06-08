def smallestDistance(target, bombs):

	number = 1000
	for bomb in bombs:
		if abs(int(bomb) - int(target)) < number:
			number = abs(int(bomb) - int(target))
	return number

raw = raw_input()
bombs = raw.split(' ')

raw = raw_input()
targets = raw.split(' ')

targets = sorted(targets)
bombs = sorted(bombs)

differences = []

for target in targets:
	differences.append(smallestDistance(target, bombs))

print max(differences)