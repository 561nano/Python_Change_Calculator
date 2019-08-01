# Provide the count of each value (highest to lowest)
countOfValue = {100: 1, 50: 10, 20: 10, 10: 10, 5: 10, 1: 10, .25: 10, .10: 1, .05: 10, .01: 10}
# Provide the change need to return
changeNeeded = 205.23
# The list that will give you the change you need to give
changeBack = []

for i in countOfValue.keys():
    changeCount = changeNeeded / i

    if changeCount >= 1 and countOfValue[i] >= int(changeCount):
        changeBack.append((i, int(changeCount)))
        changeNeeded = changeNeeded - (i * int(changeCount))
        countOfValue[i] = countOfValue[i] - int(changeCount)
    elif changeCount >= 1 and countOfValue[i] > 0:
        changeBack.append((i, countOfValue[i]))
        changeNeeded = changeNeeded - (i * countOfValue[i])
        countOfValue[i] = 0

print(changeBack)
print(countOfValue)
