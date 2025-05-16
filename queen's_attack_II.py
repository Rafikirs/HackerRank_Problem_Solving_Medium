# Exercise: Queen's Attack II
# URL: https://www.hackerrank.com/challenges/queens-attack-2/problem?isFullScreen=true
# Description:
# Calculate the number of squares a queen can attack on an n x n chessboard, given her position 
# and obstacles that block her path in any of the 8 directions

def queensAttack(n, k, r_q, c_q, obstacles):
    obstacle_set = set(map(tuple, obstacles))
    attacks_count = 0

    for i in range(1, n - r_q + 1):
        if (r_q + i, c_q) in obstacle_set:
            break
        attacks_count += 1

    for i in range(1, r_q):
        if (r_q - i, c_q) in obstacle_set:
            break
        attacks_count += 1

    for i in range(1, n - c_q + 1):
        if (r_q, c_q + i) in obstacle_set:
            break
        attacks_count += 1

    
    for i in range(1, c_q):
        if (r_q, c_q - i) in obstacle_set:
            break
        attacks_count += 1

    for i in range(1, min(n - r_q + 1, n - c_q + 1)):
        if (r_q + i, c_q + i) in obstacle_set:
            break
        attacks_count += 1

    for i in range(1, min(n - r_q + 1, c_q)):
        if (r_q + i, c_q - i) in obstacle_set:
            break
        attacks_count += 1

    for i in range(1, min(r_q, n - c_q + 1)):
        if (r_q - i, c_q + i) in obstacle_set:
            break
        attacks_count += 1

    for i in range(1, min(r_q, c_q)):
        if (r_q - i, c_q - i) in obstacle_set:
            break
        attacks_count += 1

    return attacks_count


