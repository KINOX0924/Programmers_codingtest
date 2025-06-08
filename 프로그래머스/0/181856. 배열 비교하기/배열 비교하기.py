def solution(arr1, arr2):
    total_1 = 0
    total_2 = 0
    
    for number in arr1 :
        total_1 += number
    for number in arr2 :
        total_2 += number
    
    if len(arr1) == len(arr2) :
        if total_1 > total_2 :
            return 1
        elif total_1 < total_2 :
            return -1
        elif total_1 == total_2 :
            return 0
    elif len(arr1) > len(arr2) :
        return 1
    elif len(arr1) < len(arr2) :
        return -1