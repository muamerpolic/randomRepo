infinity = 	1 << 20

dpArray = [infinity] * 50000

raw = raw_input()

noteValues = []

numberOfNotes = int(raw.split(' ')[0])
moneyToReturn = int(raw.split(' ')[1])

for i in range (numberOfNotes):
	noteValues.append(int(input()))

noteValues = sorted(noteValues)

dpArray[0] = 0

for i in range (1, moneyToReturn + 1):
	for j in range (numberOfNotes):
		if i >= noteValues[j]:
			dpArray[i] 	= min (dpArray[i], dpArray[i - noteValues[j]] + 1)
		else:
			break

if dpArray[moneyToReturn] == infinity:
	print '-1'
else:
	print dpArray[moneyToReturn]