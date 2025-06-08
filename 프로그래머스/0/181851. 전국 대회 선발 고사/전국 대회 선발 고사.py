def solution(rank, attendance):
    rank_list = []
    total = 0
    
    for index , boolean in enumerate(attendance) :
        if boolean == True :
            rank_list.append(rank[index])
    
    rank_list = list(sorted(rank_list))
    
    for index , ranks in enumerate(rank) :
        if ranks == rank_list[0] :
            total += 10000 * index
        elif ranks == rank_list[1] :
            total += 100 * index
        elif ranks == rank_list[2] :
            total += index
            
    return total