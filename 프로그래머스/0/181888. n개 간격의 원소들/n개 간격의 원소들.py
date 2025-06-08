def solution(num_list, n):
    answer = []
    
    for index in range(0 , len(num_list) , n) :
        answer.append(num_list[index])
    
    return answer