from itertools import permutations

def solution(babbling):
    shy_child = ["aya" , "ye" , "woo" , "ma"]
    count = 0
    
    lists = [
        "".join(keyword) for i in range(1,5)
        for keyword in permutations(shy_child , i)
        if sum(len(word) for word in keyword) <= 15
    ]
    
    for item in babbling :
        if item in lists :
            count += 1
    
    return count