
""" pas terminer """
def binary_search(list_num , to_search):
    arrList = []
    low  = 0
    high = len(list_num)
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        arrList.append(mid)
        # print(arrList)
        if list_num[mid] < to_search:
          low = mid + 1
        #   arrList.append(mid)
          return low
        elif list_num[mid] > to_search:
          #print(arrList)
          high = mid - 1
        #   arrList.append(high)
        else:
          return mid
    
    else: 
      return - 1




testArray = [
  0, 1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
  23, 49, 70
]





print(binary_search(testArray , 0))
#print(binary_search(list_container , 10))
