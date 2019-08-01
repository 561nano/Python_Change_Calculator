# Provide the count of each value (highest to lowest)
countOfValue = {100: 2, 50: 10, 20: 10, 10: 10, 5: 10, 1: 10, .25: 10, .10: 1, .05: 10, .01: 10}
# Provide the change need to return
changeNeeded = 200.98


# The list that will give you the change you need, what is left in the register and if there is not enough money in
# the draw to give you the total that is missing
def i_need_change(count_of_value, change_needed):
    change_back = []
    for i in count_of_value.keys():
        changeCount = change_needed / i

        if changeCount >= 1 and count_of_value[i] >= int(changeCount):
            change_back.append((i, int(changeCount)))
            change_needed = change_needed - (i * int(changeCount))
            count_of_value[i] = count_of_value[i] - int(changeCount)
        elif changeCount >= 1 and count_of_value[i] > 0:
            change_back.append((i, count_of_value[i]))
            change_needed = change_needed - (i * count_of_value[i])
            count_of_value[i] = 0

    if 0.009 <= change_needed <= 0.01:
        change_needed = 0.00
    return {"count_of_value": count_of_value, "change_back": change_back, "change_needed": change_needed}


x = i_need_change(countOfValue, changeNeeded)
print(x["count_of_value"])
print(x["change_back"])
print(x["change_needed"])

print(0.1/0.1)