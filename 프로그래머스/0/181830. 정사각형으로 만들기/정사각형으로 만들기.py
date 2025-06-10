def solution(arr):
    length_list = []
    
    if len(arr[0]) > len(arr) :
        arr += [[0 for _ in range(len(arr[0]))] for _ in range(len(arr[0]) - len(arr))]
        return arr
    # 컴프리헨션
    # arr 자체의 길이가 arr[0] 보다 낮은 경우(예시 2) 0 을 채운 리스트를 arr[0] 의 길이만큼 추가
    # 예시 2번 같은 경우 여기서 바로 return 되어 신경쓸 필요 없음
    
    for index in range(0 , len(arr)) :
        length_list.append(len(arr))
    # 2번에서 걸러내진 리스트에 대해서 arr 리스트 내의 리스트에 대한 길이값을 가져옴
    
    length_list = list(set(length_list))
    if len(length_list) == 1 and length_list[0] == len(arr[0]) :
        return arr
    else :
        for item in arr :
            if len(item) < len(arr) :
                while len(item) < len(arr) :
                    item.append(0)
        return arr
    # 예시 3
    # 길이값을 set 으로 중복 제거를 함
    # 중복 제거 시 길이값 리스트의 길이가 1 이면 모든 리스트내 리스트의 길이가 같다는 의미
    # 그리고 길이값 리스트에 있는 길이와 arr 리스트의 0 번 리스트의 길이가 같다면 수정 필요 없음
    # 따라서 arr 그대로 return
    
    