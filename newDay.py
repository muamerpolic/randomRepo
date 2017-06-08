def stepenDvojke(number):
	if not int(number) & (int(number) - 1):
		return True
	else:
		return False

raw = raw_input()
numbers = raw.split(' ')
ammount = 0.0
for number in numbers:
	if stepenDvojke(number):
		ammount += int(number)
print ammount