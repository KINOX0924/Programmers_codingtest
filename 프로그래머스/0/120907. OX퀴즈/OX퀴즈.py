def solution(quiz):
    temp = ""
    temp_list = []
    temp_temp_list = []
    result_list = []
        
    for quiz_str in quiz :
        for index , word in enumerate(quiz_str) :
            if word != " " :
                temp += word
            elif word == " " :
                temp_list.append(temp)
                temp = ""
        temp_list.append(temp)
        temp_temp_list.append(temp_list)
        temp = ""
        temp_list = []
    
    for q in temp_temp_list :
        if q[1] == "+" :
            if (int(q[0]) + int(q[2])) == int(q[4]) :
                result_list.append("O")
            else :
                result_list.append("X")
        elif q[1] == "-" :
            if (int(q[0]) - int(q[2])) == int(q[4]) :
                result_list.append("O")
            else :
                result_list.append("X")
    
    return result_list