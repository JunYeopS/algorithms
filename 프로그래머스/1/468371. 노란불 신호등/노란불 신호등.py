def solution(signals):
    answer = []
    colors_final = []
    all_yello = False
    
    for g,y,r in signals:
        colors_a = []
        for _ in range(g):
            colors_a.append("G")
        for _ in range(y):
            colors_a.append("Y")
        for _ in range(r):
            colors_a.append("R")

        colors_final.append(colors_a)    
    
    limit = len(colors_final[0])

    for i in range(1, len(colors_final)):
        cycle = len(colors_final[i])
        base = limit

        while limit % cycle != 0:
            limit += base
        
    count = 0 
    
    while not all_yello:
        
        # 각 신호등에 n번쪠를 비교해서 다르면 pass 같으면 쭉 확인 다 맞으면 정답 
        for i in range(len(signals)-1):
            tmp=colors_final[i][count%len(colors_final[i])]
            tmp2= colors_final[i+1][count%len(colors_final[i+1])]
            if tmp == "Y" and tmp2 == "Y":
                all_yello = True
            else: 
                all_yello = False
                count += 1
                break
        answer = count + 1

        if count >= limit:
            return -1
    return answer