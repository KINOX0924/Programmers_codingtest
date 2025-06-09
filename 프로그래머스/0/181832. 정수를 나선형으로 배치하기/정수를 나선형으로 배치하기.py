def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    # 0 을 n 개 가진 n 개의 리스트를 answer 리스트에 컴프리헨션
    
    x_moving = [ 0 , 1 , 0 , -1 ]   # 열간 이동
    y_moving = [ 1 , 0 , -1 , 0 ]   # 행간 이동
    moving_index = 0                # 현재의 방향 설정을 하는 변수
    
    x , y = 0 , 0               # 시작 위치 초기화
    next_x , next_y = 0 , 0     # 다음 이동 위치 초기화
    
    number = 1  # 배열에 들어갈 값
    
    while number <= n*n :
        answer[x][y] = number
        number += 1
        # x , y 좌표값에 값을 넣고 값에 + 1
        
        next_x = x + x_moving[moving_index]
        next_y = y + y_moving[moving_index]
        # 다음으로 갈 좌표를 미리 확인하기 위해서 현 좌표값에 이동값을 더한 값을 변수에 저장
        
        if 0 <= next_x < n and 0 <= next_y < n and answer[next_x][next_y] == 0 :
            x = next_x
            y = next_y
            # 다음 좌표가 범위 내에 있고, 다음 좌표값에 있는 것이 0(빈숫자) 라면 이동
        else :
            moving_index = (moving_index + 1) % 4
            # 이동값을 올리거나 내리기만 반복하면 리스트를 무한히 만들어야 할수도 있으니
            # % 4 를 사용하여 이동만 하도록 함
            x += x_moving[moving_index]
            y += y_moving[moving_index]
    
    return answer