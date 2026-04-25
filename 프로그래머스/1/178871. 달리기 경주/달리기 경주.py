def solution(players, callings):
    rank = {players[i]: i for i in range(len(players))}
    
    for cal_name in callings:  
        cur = rank[cal_name]
        
        players[cur-1],players[cur] = players[cur], players[cur-1]
  
        rank[cal_name] = cur-1 
        rank[players[cur]] = cur

    return players