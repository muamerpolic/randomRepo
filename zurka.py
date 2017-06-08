x = {}
for i in range (3):
	n = input()
	raw = raw_input()
	numbers = raw.split(' ')
	for number in numbers:
		if not number in x:
			x[number] = 1
		else:
			x[number] += 1
count = 0

print x

for key in x:
	if x[key] == 3:
		count = count + 1
print count