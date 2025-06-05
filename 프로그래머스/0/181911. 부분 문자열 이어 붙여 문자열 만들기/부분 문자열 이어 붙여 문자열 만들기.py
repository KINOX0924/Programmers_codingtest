def solution(my_strings, parts):
    answer = ""
    count = 0
    
    for string in my_strings :
        temp  = ""
        
        for index in range(parts[count][0] , parts[count][1] + 1) :
            temp += string[index]
        
        answer += temp
        count += 1
        # print(answer)
                           
                           
    return answer