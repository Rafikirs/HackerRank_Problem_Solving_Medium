# Exercise: Climbing the Leaderbord
# URL: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true
# Description:
# A player wants to track their rank after each game on a dense ranking leaderboard. In dense ranking:
# - The player with the highest score is rank 1.
# - Equal scores share the same rank.
# - The next unique score gets the next rank (no skipping).

def climbingLeaderboard(ranked, player):
    unique_ranked = sorted(set(ranked), reverse=True)
    
    result = []
    index = len(unique_ranked) - 1  
    
    for score in player:
        while index >= 0 and score >= unique_ranked[index]:
            index -= 1
        result.append(index + 2) 
    
    return result
