def solution(common):
    operation = ""
    
    if common[1] == 0 or common[2] == 0 or common[0] == 0 :
        operation = "등차수열"
    elif abs(common[1]) / abs(common[0]) == abs(common[2]) / abs(common[1]) :
        operation = "등비수열"
    else :
        operation = "등차수열"
    
    print(operation)    # 디버깅
        
    if operation == "등차수열" :
        common[-1] += common[1] - common[0]
        return common[-1]
    elif operation == "등비수열" and common[0] >= 0 and common[1] < 0 :
        common[-1] *= -(abs(common[1]) // abs(common[0]))
        return common[-1]
    elif operation == "등비수열" :
        common[-1] *= abs(common[1]) // abs(common[0])
        return common[-1]