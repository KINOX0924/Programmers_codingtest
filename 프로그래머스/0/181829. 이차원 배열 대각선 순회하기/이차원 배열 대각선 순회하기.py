def solution(board, k):
    total = 0
    i = 0
    j = 0
    
    while i < len(board) :
        if i + j <= k :
            total += board[i][j]
            
        j += 1
        if j == len(board[0]) :
            j = 0
            i += 1
            
    return total