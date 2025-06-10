def solution(array) :
    result = []
    for index , number in enumerate(array) :
        if len(result) == 0 :
            result.append(number)
            result.append(index)
        
        if result[0] < number :
            result[0] = number
            result[1] = index
    
    return result