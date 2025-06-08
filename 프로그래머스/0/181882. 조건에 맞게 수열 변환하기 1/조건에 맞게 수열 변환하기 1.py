def solution(arr):
    answer = []
    
    for index , number in enumerate(arr) :
        if number >= 50 and number % 2 == 0 :
            arr[index] = number // 2
        elif number < 50 and number % 2 == 1 :
            arr[index] = number * 2
    
    return arr
    
    return answer