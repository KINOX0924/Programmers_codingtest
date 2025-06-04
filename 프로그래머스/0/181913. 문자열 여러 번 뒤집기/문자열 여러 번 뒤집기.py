def solution(my_string, queries):
    answer = ''
    
    str_list = [word for word in my_string]
    
    for i in range(0,len(queries)) :
        comp_list = []
        count = 0
        for index in range(queries[i][1] , queries[i][0] -1 , -1) :
            comp_list.append(str_list[index])
            # print(comp_list)    # 디버깅
            
        for index in range(queries[i][0] , queries[i][1] + 1) :
            str_list[index] = comp_list[count]
            count += 1
            # print(str_list)     # 디버깅
            
    answer = "".join(str_list)
    
    return answer