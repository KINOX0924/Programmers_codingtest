def solution(q, r, code):
    answer = ''
    
    for index , word in enumerate(code) :
        if index % q == r :
            answer += word
    
    return answer