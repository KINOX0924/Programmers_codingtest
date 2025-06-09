def solution(myString):
    temp_list = []
    
    for index , ch in enumerate(myString) :
        if ch in "abcdefghijk" :
            temp_list.append("l")
        else :
            temp_list.append(ch)
    
    temp_list = "".join(temp_list)
    
    return temp_list