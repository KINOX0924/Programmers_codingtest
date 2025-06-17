def divider(polynomial) :
    temp = ""
    var_list = []
    num_list = []
    
    for char in polynomial :
        if   char != " " and char != "+" :
            temp += char
        elif char == " " and temp != "" :
            if temp[-1] == "x" :
                var_list.append(temp)
            elif temp.isdigit() :
                num_list.append(int(temp))
            temp = ""
            
    if temp[-1] == "x" :
        var_list.append(temp)
    elif temp.isdigit() :
        num_list.append(int(temp))
    
    # print(var_list)      # 디버깅
    # print(num_list)      # 디버깅
    return var_list , num_list

def calculator(var_list) :
    sum_count = 0
    
    for var in var_list :
        if var[0].isdigit() :
            sum_count += int(var[0:-1])
        elif var[0] == "x" :
            sum_count += 1
    # print(f"sum : {sum_count}") # 디버깅
    
    return sum_count

def solution(polynomial):
    var_list , num_list = divider(polynomial)
    sum_count = calculator(var_list)
    
    if sum_count == 1 and len(num_list) != 0 :
        answer = "x" + " + " + str(sum(num_list))
    elif sum_count == 1 and len(num_list) == 0 :
        answer = "x"
    elif len(num_list) != 0 and len(var_list) != 0 :
        answer = str(sum_count) + "x" + " + " + str(sum(num_list))
    elif len(num_list) == 0 :
        answer = str(sum_count) + "x"
    elif len(var_list) == 0 :
        answer = str(sum(num_list))
        
    return answer