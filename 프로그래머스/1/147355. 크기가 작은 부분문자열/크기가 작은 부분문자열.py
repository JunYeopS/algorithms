def solution(t, p):
    p_len = len(p)
    
    answer = 0

    for i in range(len(t)-p_len+1):
        if int(t[i:p_len+i]) <= int(p):
            answer += 1

    return answer