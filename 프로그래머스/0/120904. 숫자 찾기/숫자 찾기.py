def solution(num, k):
    index = str(num).find(str(k))
    
    if index >= 0 :
        return index + 1
    return -1