def solution(n):
    lists = []
    
    for i in range(0 , n) :
        temp_list = []
        for j in range(0 , n) :
            if i == j :
                temp_list.append(1)
            else :
                temp_list.append(0)
        lists.append(temp_list)
    
    return lists