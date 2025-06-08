def solution(names):
    answer = []
    
    for index , name in enumerate(names) :
        if index % 5 == 0 :
            answer.append(name)
            
    
    return answer