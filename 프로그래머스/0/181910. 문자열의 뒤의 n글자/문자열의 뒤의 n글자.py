def solution(my_string, n):
    answer = ''
    
    for index in range(len(my_string) - n , len(my_string)) :
        answer += my_string[index]
    
    return answer