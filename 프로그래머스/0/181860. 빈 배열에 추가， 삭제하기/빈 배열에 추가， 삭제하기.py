def solution(arr, flag):
    answer = []
    count  = 0
    
    for boolean in flag :
        if boolean == True :
            for index in range(0,arr[count] * 2) :
                answer.append(arr[count])
        elif boolean == False :
            for index in range(0, arr[count]) :
                answer.pop()
        count += 1
    
    return answer