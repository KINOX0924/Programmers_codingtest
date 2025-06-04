def solution(code):
    mode = 0
    temp_list = []
    ret = []
    answer = ''

    for word in code :
        temp_list.append(word)

    for index , word in enumerate(temp_list) :
        if mode == 0 and index % 2 == 0 and word != "1" :
            ret.append(word)
        elif mode == 0 and word == "1" :
            mode = 1
        elif mode == 1 and index % 2 == 1 and word != "1" :
            ret.append(word)
        elif mode == 1 and word == "1" :
            mode = 0
    
    if len(ret) <= 0 :
        return "EMPTY"
    
    answer = "".join(ret)

    return answer