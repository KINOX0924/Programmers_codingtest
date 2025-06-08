def solution(todo_list, finished):
    answer = []
    
    for index , isfinish in enumerate(finished) :
        if isfinish == False :
            answer.append(todo_list[index])
    
    return answer