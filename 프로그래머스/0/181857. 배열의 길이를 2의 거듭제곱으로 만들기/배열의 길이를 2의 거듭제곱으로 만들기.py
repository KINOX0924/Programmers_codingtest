def solution(arr):
    two_list = [1,2,4,8,16,32,64,128,256,512]
    length = len(arr)
    end_count = 1
    
    while end_count < length :
        end_count *= 2
    
    arr += [0] * (end_count - length)
    

    return arr