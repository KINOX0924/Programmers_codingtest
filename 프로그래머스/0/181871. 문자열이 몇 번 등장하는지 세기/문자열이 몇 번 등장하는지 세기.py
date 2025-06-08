# 정말로 프로그래밍을 해본 사람이 문제를 만든 건가?
# aaaa 에서 4번 인덱스가 어디 있다는 거야?
# 0 ~ 4 번 인덱스면 aaaaa 여야지

def solution(myString, pat):
    answer = 0
    end    = len(pat)
    
    for i in range(0 , len(myString)) :
        if myString[i:end] == pat :
            answer += 1
        end += 1
    
    return answer