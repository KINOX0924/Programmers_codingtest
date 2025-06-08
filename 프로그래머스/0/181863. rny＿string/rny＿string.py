def solution(rny_string):
    answer = ''
    
    for word in rny_string :
        if word != "m" :
            answer += word
        elif word == "m" :
            answer += "rn"
    
    return answer