def solution(rsp):
    RPS = {"2" : 0 , "0" : 5 , "5" : 2}
    win = ""
    
    for char in rsp :
        win += str(RPS[char])
    
    return win