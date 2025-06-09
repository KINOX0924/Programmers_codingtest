def solution(picture, k):
    temp_list = []
    temp = ""
    
    for string in picture :
        for word in string :
            count = 1
            while count <= k :
                temp += word
                count += 1
        count_2 = 1
        while count_2 <= k :
            temp_list.append(temp)
            count_2 += 1
        temp = ""
    
    return temp_list