def getSide(sides) :
    max_side = max(sides)
    min_side = min(sides)
    possible_sides = []
    
    # [1] 가장 긴 변을 기준으로 선분을 구하는 경우
    # 남은 두 개의 선분의 합이 가장 긴 변보다는 크면서 각 변의 길이가 가장 긴 변 보다는 작은 수
    for side in range(1 , max_side + 1) :
        if side + min_side > max_side and side <= max_side :
            possible_sides.append(side)
    
    # print(possible_sides)   # 디버깅
    
    # [2] 주어진 두 개 선분의 길이를 합친 뒤 최대 선분의 길이와 합친 선분 길이의 미만 선분을 구함
    for side in range(max_side + 1 , min_side + max_side) :
        if side not in possible_sides :
            possible_sides.append(side)
    
    # print(possible_sides)   # 디버깅
    
    return possible_sides

def solution(sides) :
    possible_sides = getSide(sides)
    
    return len(possible_sides)
    