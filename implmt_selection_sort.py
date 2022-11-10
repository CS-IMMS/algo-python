def selectionSort(array):
    size = len(array)
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])
 
arr = [1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]
#size = len(arr)
selectionSort(arr)
print(arr)