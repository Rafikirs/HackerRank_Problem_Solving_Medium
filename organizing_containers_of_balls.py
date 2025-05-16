# Exercise: Organizing Containers of Balls
# URL: https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem?isFullScreen=true
# Description: 
# Determine if balls can be sorted such that each container holds only one type of ball 
# using only swaps between containers

def organizingContainers(containers):
    container_sizes = []
    ball_numbers = []
    
    for container in containers:
        container_sizes.append(sum(container))
                
    for i in range(len(containers[0])):
        ball_numbers.append(sum([x[i] for x in containers]))
    
    possible = (sorted(ball_numbers) == sorted(container_sizes))
    
    if possible == True:
        return "Possible"
        
    else:
        return "Impossible"
