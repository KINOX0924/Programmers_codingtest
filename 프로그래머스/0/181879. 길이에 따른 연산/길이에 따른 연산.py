def solution(num_list):
    answer = 0
    
    if len(num_list) >= 11 :
        answer = sum(num_list)
    else :
        answer = num_list[0]
        for index in range(1 , len(num_list)) :
            answer *= num_list[index]
    
    return answer