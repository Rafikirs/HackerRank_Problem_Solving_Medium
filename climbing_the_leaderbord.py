def climbingLeaderboard(ranked, player):
    unique_ranked = sorted(set(ranked), reverse=True)
    
    result = []
    index = len(unique_ranked) - 1  
    
    for score in player:
        while index >= 0 and score >= unique_ranked[index]:
            index -= 1
        result.append(index + 2) 
    
    return result
