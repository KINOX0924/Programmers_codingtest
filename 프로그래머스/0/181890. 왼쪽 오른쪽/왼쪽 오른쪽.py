def solution(str_list):
    answer     = []
    left_list  = []
    right_list = []
    
    if "l" not in str_list and "r" not in str_list :
        return answer

    for index , word in enumerate(str_list) :
        if len(left_list) == 0 and word == "l" :
            return answer
        elif word != "l" and word != "r" :
            left_list.append(word)
        elif len(left_list) > 0 and word == "l" :
            answer = left_list
            return answer
        elif word == "r" :
            for i in range(index + 1 , len(str_list)) :
                answer.append(str_list[i])
            return answer
    
    return answer