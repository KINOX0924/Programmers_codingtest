def solution(intStrs, k, s, l):
    answer = []
    
    for number in intStrs :
        text_number = ""
        for i in range(s , s + l) :
            text_number += number[i]
            print(text_number)
        if int(text_number) > k :
            answer.append(int(text_number))
        
        # print(answer)
    
    return answer