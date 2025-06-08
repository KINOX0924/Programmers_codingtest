def solution(arr):
    answer = []
    min_index = None
    max_index = None
    
    for index in range(0 , len(arr)) :
        if arr[index] == 2 and min_index == None :
            min_index = int(index)
            max_index = int(index)
        elif arr[index] == 2 and max_index != None :
            max_index = int(index)
    
    if min_index == None and max_index == None :
        answer.append(-1)
        return answer
        
    for index in range(min_index , max_index + 1) :
        answer.append(arr[index])
        
    return answer