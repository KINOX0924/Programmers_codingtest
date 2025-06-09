def solution(date1, date2):

    for index in range(0 , len(date1)) :
        if index == 0 :
            if date1[index] < date2[index] :
                return 1
            elif date1[index] > date2[index] :
                return 0
        elif index == 1 :
            if date1[index] < date2[index] :
                return 1
            elif date1[index] > date2[index] :
                return 0
        elif index == 2 :
            if date1[index] < date2[index] :
                return 1
            else :
                return 0