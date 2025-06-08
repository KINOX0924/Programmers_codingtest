def solution(arr, n):
    if len(arr) % 2 == 0 :
        for index in range(0,len(arr)) :
            if index % 2 == 1 :
                arr[index] += n
    elif len(arr) % 2 == 1 :
        for index in range(0,len(arr)) :
            if index % 2 == 0 :
                arr[index] += n
    
    return arr