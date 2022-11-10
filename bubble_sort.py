

def bubbleSort(arr):
    n = len(arr)
    change = False
    arrBuld =[]
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                change = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not change:
            return
    for i in range(len(arr)):
        arrBuld.append(arr[i]) 
    return arrBuld
 
# Driver code to test above
arr = [4,2,8,345,123,43,32,2,1,5643,63,123,43,2,55,1,234,92]
 
print(bubbleSort(arr))
 
