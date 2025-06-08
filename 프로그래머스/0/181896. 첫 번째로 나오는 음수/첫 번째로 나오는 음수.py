def solution(num_list):
    answer = 0
    
    for index in range(0 , len(num_list)) :
        if num_list[index] < 0 :
            answer = index
            return answer
    
    answer = -1
    
    return answer