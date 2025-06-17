def solution(dot):
    if dot[0] >= 1 and dot[1] >= 1 :
        return 1
    elif dot[0] >= 1 and dot[1] < 0 :
        return 4
    elif dot[0] < 0 and dot[1] < 0 :
        return 3
    else :
        return 2