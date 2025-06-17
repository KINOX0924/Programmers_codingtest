def searchBomb(board , searched_map) :
    dx = [ 0 , 0 , -1 , 1 , -1 , 1 , 1 , -1 ]
    dy = [ -1 , 1 , 0 , 0 , -1 , -1 , 1 , 1 ]
    count = 0
    
    for col in range(len(board)) :
        for row in range(len(board)) :
            if searched_map[col][row] == 0 and board[col][row] == 1 :
                searched_map[col][row] = "위험"
                count += 1
                for angle in range(len(dx)) :
                    n_col = col + dx[angle]
                    n_row = row + dy[angle]
                    if n_col < 0 or n_col >= len(board) or n_row < 0 or n_row >= len(board) :
                        continue
                    if board[n_col][n_row] != 1 and searched_map[n_col][n_row] != "위험" :
                        searched_map[n_col][n_row] = "위험"
                        count += 1
    
    return searched_map , count

def solution(board):
    searched_map = [ [0] * len(board) for _ in range(len(board)) ]
    searched_map , count = searchBomb(board , searched_map)
                              
    # print(searched_map)   # 디버깅
    # print(count)          # 디버깅
    
    return (len(board)) * (len(board)) - count