# 제발 문제 좀 똑바로 썼으면 좋겠다.
# 가장 긴 부분 문자열이 아니잖아, 진짜 문제를 이해 더럽게 안되게 써놨네
# 프로그래머식 사고방식을 운운하기 전에 문제를 작성한 사람이 국어를 더럽게 못했을 거라는 것 만큼은 알 것 같다.

def solution(myString, pat):
    answer = ''
    end_index = myString.rfind(pat) + len(pat)
    
    for index in range(0 , end_index) :
        answer += myString[index]
    
    return answer