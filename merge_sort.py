


def mergeSort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        midle = len(arr) //2
        left = mergeSort(arr[:midle])
        right = mergeSort(arr[midle:])
        return merge(left,right)

def merge(left,rigth):
    result =[]
    i,j = 0,0
    while i < len(left) and j < len(rigth):
        if left[i] < rigth[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(rigth[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(rigth):
        result.append(rigth[j])
        j += 1
    return result

test =  mergeSort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92])

print(test)