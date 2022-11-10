


def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        comp_elemt = arr[i]
        while i > 0 and comp_elemt < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i = i-1
    return arr

test = insertionSort([5, 4, 33, 2, 8,1,-5])
print(test)