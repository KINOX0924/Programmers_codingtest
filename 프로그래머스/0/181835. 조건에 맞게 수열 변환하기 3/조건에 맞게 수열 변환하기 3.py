def solution(arr, k):
    if k % 2 == 1 :
        for index , number in enumerate(arr) :
            arr[index] = number * k
    elif k % 2 == 0 :
        for index , number in enumerate(arr) :
            arr[index] = number + k
    
    return arr