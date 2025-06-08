def solution(num_list):
    sorted_list = list(sorted(num_list))
    answer_list = []
    
    for index in range(5,len(sorted_list)) :
        answer_list.append(sorted_list[index])
    
    return answer_list