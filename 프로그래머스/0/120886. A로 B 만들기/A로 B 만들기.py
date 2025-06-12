def remainCounter(string) :
    remain_counting = {}
    
    for char in string :
        if char not in remain_counting.keys() :
            remain_counting[char] = 1
        else :
            remain_counting[char] += 1
    
    return remain_counting

def metch(string , count = {}) :
    
    for char in string :
        if char in count.keys() and count[char] > 0 :
            count[char] -= 1
        elif char not in count.keys() :
            return 0
        else :
            return 0
    return 1
        

def solution(before, after) :
    remain_count = remainCounter(after)
    result = metch(before , remain_count)
    
    return result