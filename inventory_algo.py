



def updateInventory(arr1, arr2):
    for i in range(len(arr2)):
        checking = False
        for j in range(len(arr1)):
            if arr2[i][1] == arr1[j][1]:
                arr1[j][0] = arr1[j][0] + arr2[i][0]
                checking =True
        if not checking:
            arr1.append(arr2[i])
    return arr1 #bubbleSort(arr1)


curInv = [[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]]

newInv = [[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]], [[2, "Hair Pin"], [3, "Half-Eaten Apple"], [67, "Bowling Ball"], [7, "Toothpaste"]]
print(updateInventory([[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]], [[2, "Hair Pin"], [3, "Half-Eaten Apple"], [67, "Bowling Ball"], [7, "Toothpaste"]]))


