from collections import deque

def solution(A, B):
    count = 0
    T = 0
    A_cp = deque()
    
    if A == B :
        return 0
    
    for ch in A :
        A_cp.append(ch)

    for ch in A :
        A_cp.appendleft(A_cp.pop())
        string = "".join(A_cp)
        count += 1
        if string == B :
            T += 1
            return count
    
    if T == 0 :
        return -1
            