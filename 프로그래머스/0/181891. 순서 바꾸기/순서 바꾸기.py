def solution(num_list, n):
    answer = []
    front_list = []
    rear_list  = []

    for index , number in enumerate(num_list) :
        if index <= n - 1 :
            front_list.append(number)
        else :
            rear_list.append(number)
    
    answer = rear_list + front_list
    
    return answer