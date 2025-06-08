def solution(num_list, n):
    answer = []
    
    for index , number in enumerate(num_list) :
        if index >= n - 1 :
            answer.append(number)
    
    return answer