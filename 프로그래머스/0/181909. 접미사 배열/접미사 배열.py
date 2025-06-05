def solution(my_string):
    answer = []
    start  = 0
    
    for i in range(0,len(my_string)) :
        temp = ""
        for j in range(start , len(my_string)) :
            temp += my_string[j]
        answer.append(temp)
        start += 1
    
    answer = list(sorted(answer))

    return answer