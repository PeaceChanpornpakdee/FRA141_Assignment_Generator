# Problem #

# Solution #
def checkStock (stockList):
    itemList = []
    amountList = []

    for s in stockList:
        if s not in itemList:
            itemList.append(s)
            amountList.append(1)

        else:
            idx = itemList.index(s)
            amountList[idx] += 1

    ansList = []

    for i in range(len(itemList)):
        ansList.append([ itemList[i] , amountList[i] ])

    ansList = sorted(ansList)

    return ansList

# Example #

# Test cases #
print( checkStock ( ["Carrot", "Apple", "Carrot", "Egg"] ) )
print( checkStock ( ["Meat", "Pea", "Pea", "Pea", "Potato", "Potato"] ) )
print( checkStock ( ["Onion", "Ginger", "Garlic", "Cucumber", "Corn", "Cabbage"] ) )
print( checkStock ( ["Egg", "Egg", "Egg", "Egg", "Egg", "Egg", "Egg", "Egg", "Egg", "Egg", "Egg", "Egg"] ) )
print( checkStock ( ["Eggplant", "Egg", "Eggplant", "Egg", "Eggplant", "Egg", "Eggplant", "Egg", "Eggplant", "Egg", "Eggplant", "Egg", "Eel", "Egg"] ) )
print( checkStock ( [] ) )
