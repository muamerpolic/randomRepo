def smallestPrice (startPos, L, duration):
	minEl = 1000
	
	if startPos <= duration:
		L = L[0 : startPos]
	else:
		L = L[startPos - duration: startPos]
	for i in L:
		if i < minEl:
			minEl = i
	print L, minEl
	return minEl



raw = raw_input()
l = []
n = int(raw.split(' ')[0])
d = int(raw.split(' ')[1])
for i in range (n):
	temp = input()
	l.append(temp)

sol = 0

for i in range(1, 9):
	sol += smallestPrice(i, l, d)
print sol