


def QuickSort(arr):
    elment = len(arr)

    if elment < 2:
        return arr
    curr_position = 0
    for i in range(1,elment):
        if arr[i] <= arr[0]:
            curr_position += 1
            portion = arr[i]
            arr[i] = arr[curr_position]
            arr[curr_position] = portion
    portion = arr[0]
    arr[0] = arr[curr_position]
    arr[curr_position] = portion
    
    # sorted elemnt to the left in right pivot
    left = QuickSort(arr[0:curr_position])
    right = QuickSort(arr[curr_position +1: elment])
    arr = left + [arr[curr_position]] + right
    return arr

test = [1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]

print(QuickSort(test))
