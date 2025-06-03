def solution(str1, str2):
    answer = ''
    
    str1_list = []
    str2_list = []
    sum_list  = []
    
    count     = 0
    
    for word in str1 :
        str1_list.append(word)
        count += 1
        
    for word in str2 :
        str2_list.append(word)
        
    for i in range(0,count) :
        sum_list.append(str1_list[i])
        sum_list.append(str2_list[i])
        
    answer = "".join(sum_list)
    
    
    return answer