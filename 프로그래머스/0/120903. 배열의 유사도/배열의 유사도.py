def solution(s1, s2):
    count = 0
    
    if len(s1) > len(s2) :
        for word in s1 :
            if word in s2 :
                count += 1
    elif len(s2) > len(s1) :
        for word in s2 :
            if word in s1 :
                count += 1
    elif len(s1) == len(s2) :
        for word in s2 :
            if word in s1 :
                count += 1
    
    return count