def move_merssg(keyinput , x_max , y_max) :
    direction   = {"up" : 0 , "down" : 1 , "left" : 2 , "right" : 3}
    x_direction = [ 0 , 0 , -1 , 1 ]
    y_direction = [ 1 , -1 , 0 , 0 ]
    
    now_point = [0,0]
    
    for key in keyinput :
        if (-x_max) <= now_point[0] + x_direction[direction[key]] <= x_max :
            now_point[0] += x_direction[direction[key]]
        if (-y_max) <= now_point[1] + y_direction[direction[key]] <= y_max :
            now_point[1] += y_direction[direction[key]]
            
    # print(now_point)  # 디버깅
    
    return now_point
        

def solution(keyinput, board):
    x_max = board[0] // 2
    y_max = board[1] // 2
    
    now_point = move_merssg(keyinput , x_max , y_max)
    # print(x_max)  # 디버깅
    # print(y_max)  # 디버깅
    
    return now_point