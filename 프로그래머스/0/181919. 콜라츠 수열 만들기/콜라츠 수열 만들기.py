def solution(n):
    answer = []
    
    list = [n]
    index = 0
    
    while True :
        if list[index] % 2 == 0 :
            list.append(list[index] // 2)
        elif list[index] % 2 == 1 :
            list.append(3 * list[index] + 1)
        
        if list[index + 1] == 1 :
            answer = list
            return answer
        else :
            index += 1

    return answer