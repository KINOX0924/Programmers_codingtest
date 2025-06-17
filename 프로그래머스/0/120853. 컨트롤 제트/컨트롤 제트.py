def calculator(string) :
    total    = 0
    num_list = string.split(" ")
    print(num_list) # 디버깅
    
    for index , item in enumerate(num_list) :
        if item != "Z" :
            total += int(item)
            print(item)
        elif item == "Z" :
            if int(num_list[index-1]) >= 0 :
                total -= int(num_list[index- 1])
            else :
                total += abs(int(num_list[index- 1]))
    
    return total

def solution(s):
    total = calculator(s)
    
    return total