def solution(emergency):
    queue_count = []
    queue_count_dict = {}
    sort_emer   = list(sorted(emergency , reverse = True))
    
    for sequence in range(0 , len(sort_emer)) :
        queue_count_dict[sort_emer[sequence]] = sequence + 1
    
    # print(queue_count_dict) # Debug
    
    for sequence in emergency :
        queue_count.append(queue_count_dict[sequence])
    
    # print(queue_count)  # Debug
    
    return queue_count