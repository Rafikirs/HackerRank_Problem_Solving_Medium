# Exercise: The Bomberman Game
# URL: https://www.hackerrank.com/challenges/bomber-man/problem?isFullScreen=true
# Description: Playing Bomberman on a grid

def bomberMan(n, grid):
    if n == 1:
        return grid
    if n % 2 == 0:
        return ["O" * len(grid[0]) for _ in range(len(grid))]
    
    def detonate(current):
        R, C = len(current), len(current[0])
        exploded = [['O'] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if current[i][j] == 'O':
                    exploded[i][j] = '.'
                    if i > 0:
                        exploded[i-1][j] = '.'
                    if i < R-1:
                        exploded[i+1][j] = '.'
                    if j > 0:
                        exploded[i][j-1] = '.'
                    if j < C-1:
                        exploded[i][j+1] = '.'
        return ["".join(row) for row in exploded]

    first_explosion = detonate(grid)
    second_explosion = detonate(first_explosion)

    return first_explosion if n % 4 == 3 else second_explosion
