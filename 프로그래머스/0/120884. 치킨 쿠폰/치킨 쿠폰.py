def solution(coupon):
    bouns_chicken = 0
    
    if coupon < 10 :
        return 0
    
    while coupon >= 10 :
        temp = 0
        # 보너스 치킨을 먹으면서 추가로 받은 쿠폰을 저장할 임시 변수 / 매번 초기화 필요
        # 보너스 치킨의 수 == 추가로 받은 쿠폰의 수
        
        bouns_chicken += coupon // 10
        # [1] 받은 쿠폰의 나누기 10 만큼을 보너스 치킨에 넣음
        # bouns_chicken = 10 / coupon = 100
        
        temp += coupon // 10
        # [2] 상기 내용에 따라 보너스 치킨의 수 만큼을 임시 변수에도 넣어줌
        
        coupon += temp
        # [3] 쿠폰의 수에 추가로 받은 쿠폰의 수 만큼을 더해줌
        
        coupon -= temp * 10
        # [4] 보너스 치킨을 먹기 위해 사용한 쿠폰의 수 만큼을 쿠폰에서 빼줌
    
    return bouns_chicken