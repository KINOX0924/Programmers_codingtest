def solution(array):
    count = 0
    
    for item in array :
        temp = str(item)
        for number in temp :
            if number == "7" :
                count += 1
    
    return count