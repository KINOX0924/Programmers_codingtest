def solution(num_list):
    answer = []
    list_len = len(num_list)
    
    if num_list[list_len - 1] > num_list[list_len - 2] :
        num_list.append(num_list[list_len - 1] - num_list[list_len - 2])
    else :
        num_list.append(num_list[list_len -1]*2)
    
    answer = num_list
    
    return answer