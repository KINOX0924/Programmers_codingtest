def avgScore(list) :
    score_list = []
    ranks = []
    
    for score in list :
        score_list.append((score[0] + score[1]) / 2)
    print(score_list)   # 디버깅

    rank_dict = rankScore(sorted(score_list , reverse = True))
    
    for score in score_list :
        ranks.append(rank_dict[str(score)])
    
    return ranks

def rankScore(list) :
    rank_dict = {}
    rank = 1
    
    for score in list :
        if str(score) not in rank_dict.keys() :
            rank_dict[str(score)] = rank
        rank += 1
    
    return rank_dict

def solution(score):
    rank_list = avgScore(score)
    
    return rank_list