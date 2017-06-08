guestEntrance = [0] * 10000

n = input()
maxNum = 0

for i in range (n):
	raw = raw_input()
	numbers = raw.split(' ')
	guestEntrance[int(numbers[0])] += 1
	guestEntrance[int(numbers[1]) + 1] -= 1
	if int(numbers[1]) > maxNum:
		maxNum = int(numbers[1])

maxPeople = 0
currentPeople = 0

for i in range (maxNum):
	currentPeople += int (guestEntrance[i])
	print i, currentPeople
	if currentPeople > maxPeople:
		maxPeople = currentPeople

print maxPeople