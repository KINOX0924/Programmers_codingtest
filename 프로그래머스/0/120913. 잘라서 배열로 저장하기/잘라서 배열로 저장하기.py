def solution(my_str, n):
    temp   = ""
    count  = 0
    result = []
    
    for ch in my_str :
        if count == n :
            result.append(temp)
            temp = ""
            count = 0
        temp += ch
        count += 1
    
    result.append(temp)
    
    return result