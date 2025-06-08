def solution(my_string, indices):
    answer = ''
    
    for index , word in enumerate(my_string) :
        if index not in indices :
            answer += word
    
    return answer