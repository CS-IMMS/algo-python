

def sym_for_tow_array(a,b):
    arr = a + b
    last_arr = []
    new_arr = []
    for i in range(len(arr)-1):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                last_arr.append(arr[i])
    for i in arr:
        if i not in last_arr:
            new_arr.append(i)
    return new_arr

def sym(*args):
    result = args[0]
    for i in range(1, len(args)):
        result = sym_for_tow_array(result, args[i])
    return result


    #return arrgs.__reduce__(syms)
a =[1, 2, 3]
b = [2, 3, 4]
print(sym([1, 1, 16,90,2, 5], [2,8, 2,3,3,3, 3, 5], [3, 4, 5, 5]))
