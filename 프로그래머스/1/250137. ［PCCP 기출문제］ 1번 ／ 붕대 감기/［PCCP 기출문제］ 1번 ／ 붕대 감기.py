def solution(bandage, health, attacks):
    answer = []
    
    work_time, heal, addition_heal = bandage
    tmp_health = health

    tic = 0 
    end_tic = (attacks[-1][0])
    
    count_add_heal = 0   # 추가 힐 조건 check 
    
    while end_tic != tic:
        
        tic += 1
        is_attacked = False

        # check attack 
        for i,j in attacks:
            if tic == i:
                tmp_health -= j
                count_add_heal = 0
                is_attacked =True

        # check heal
        if not is_attacked:
            count_add_heal+=1
            if count_add_heal == work_time : 
                tmp_health += addition_heal
                count_add_heal = 0
                
            if tmp_health < health:
                tmp_health += heal    
                        # 초과 방지 
            if tmp_health > health:
                tmp_health = health
                
        if tmp_health <= 0 :
            return -1
    return tmp_health