def solution(t, p):
    t_len = len(t)
    p_len = len(p)
    
    ls = list(t)
    
    answer = 0

    for i in range(t_len-(p_len-1)):
        
        tmp = (ls[i:p_len+i])
        part_num = int("".join(tmp))
        
        if part_num <= int(p):
            answer += 1
        
    return answer

