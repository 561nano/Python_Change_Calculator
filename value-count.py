# Provide the value you want to use (US currency [common])
valueList = [100, 50, 20, 10, 5, 1, .25, .10, .05, .01]
# Provide the count of each value
countOfValue = {100: 10, 50: 10, 20: 10, 10: 10, 5: 10, 1: 10, .25: 10, .10: 1, .05: 10, .01: 10}
# Provide the change need to return
changeNeeded = 105.23
# The list that will give you the change you need to give
changeBack = []

for i in valueList:
    changeCount = changeNeeded / i

    if changeCount >= 1 and countOfValue[i] >= int(changeCount):
        changeBack.append((i, int(changeCount)))
        changeNeeded = changeNeeded - (i * int(changeCount))

print(changeBack)

