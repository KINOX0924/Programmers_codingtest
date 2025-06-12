def solution(sides):
    max_length = max(sides)
    count = 0
    
    for number in sides :
        if number == max_length :
            count += 1
    
    if count == 1 :
        etc_length = [side for side in sides if side != max_length]
    else :
        etc_length = [side for side in sides if side != max_length]
        etc_length.append(max_length)
    
    if sum(etc_length) > max_length :
        return 1
    elif sides[0] == sides[1] == sides[2] :
        return 1
    return 2