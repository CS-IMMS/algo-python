


def pairwise(arr, numb):
    sum_idx = 0
    list_idx = []
    for i in range(len(arr)):
        for j in range(i +1,len(arr)):
            if arr[i] + arr[j] == numb:
                if i not in list_idx and j not in list_idx:
                    list_idx.append(i)
                    list_idx.append(j)
                    sum_idx += i + j
    return sum_idx
test = pairwise([1,4,2,3,0,5], 7)
print(test)
