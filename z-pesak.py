def movePosition (durationOnPositionMap, currentPosition, xAxis, yAxis, maxTime):
	xCoordinate = int(currentPosition.split(',')[0]) + xAxis
	yCoordinate = int(currentPosition.split(',')[1]) + yAxis

	newPosition = str(xCoordinate) + ',' + str(yCoordinate)


	if not newPosition in durationOnPositionMap:
		durationOnPositionMap[newPosition] = 1
	else:
		durationOnPositionMap[newPosition] += 1
	if durationOnPositionMap[newPosition] > maxTime:
		maxTime = durationOnPositionMap[newPosition]
	return newPosition, maxTime


durationOnPositionMap = {}

numberOfMoves = int(input())

currentPosition = '0,0'

durationOnPositionMap[currentPosition] = 1

maxTime = 1

for i in range (numberOfMoves):
	inputString = raw_input()
	if inputString == 'Levo':
		currentPosition, maxTime = movePosition(durationOnPositionMap, currentPosition, -1, 0, maxTime)
	if inputString == 'Desno':
		currentPosition, maxTime = movePosition(durationOnPositionMap, currentPosition, 1, 0, maxTime)
	if inputString == 'Gore':
		currentPosition, maxTime = movePosition(durationOnPositionMap, currentPosition, 0, 1, maxTime)
	if inputString == 'Dole':
		currentPosition, maxTime = movePosition(durationOnPositionMap, currentPosition, 0, -1, maxTime)
	else:
		currentPosition, maxTime = movePosition(durationOnPositionMap, currentPosition, 0, 0, maxTime)



print maxTime
	
	


