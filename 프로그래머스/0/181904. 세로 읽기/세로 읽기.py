def solution(my_string, m, c):
    answer = ''
    count  = 0
    string_list = []
    
    for i in range(0,m) :
        string_list.append([])
        
    for word in my_string :
        string_list[count].append(word)
        count += 1
        
        if count >= m :
            count = 0
    
    answer = "".join(string_list[c - 1])
    
    return answer