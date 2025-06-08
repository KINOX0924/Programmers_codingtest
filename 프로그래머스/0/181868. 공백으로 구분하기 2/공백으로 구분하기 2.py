def solution(my_string):
    answer = []
    temp = ""
    temp_list = []
    
    for word in my_string :
        if word == " " :
            temp_list.append(temp)
            temp = ""
        elif word != " " :
            temp += word
    temp_list.append(temp)
    
    for string in temp_list :
        if len(string) >= 1 :
            answer.append(string)
            
    
    return answer