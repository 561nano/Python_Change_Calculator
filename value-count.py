# Provide the value you want to use (US currency [common])
valueList = [100, 50, 20, 10, 5, 1, .25, .10, .05, .01]
# Provide the count of each value
countOfValue = {100: 10, 50: 9, 20: 8, 10: 7, 5: 6, 1: 5, .25: 4, .10: 3, .05: 2, .01: 1}
# Provide the change need to return
changeNeeded = 105.23
# The list that will give you the change you need to give
changeBack = []

for i in valueList:
    print(i)
    multiplier = changeNeeded / i
    Continue = changeNeeded % i

    if multiplier >= 1:
        changeBack.append((i, int(multiplier)))
        changeNeeded = changeNeeded - (int(multiplier) * i)

print(changeBack)

