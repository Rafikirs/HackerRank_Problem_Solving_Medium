# Exercise: 3D Surface Area
# URL: https://www.hackerrank.com/challenges/3d-surface-area/problem?isFullScreen=true
# Description: Find the area of a 3D surface

def surfaceArea(A):
    H = len(A)
    W = len(A[0]) if H>0 else 0
    area = 0

    for i in range(H):
        for j in range(W):
            if A[i][j] > 0:
                area += 2


    for i in range(H):
        for j in range(W):
            h = A[i][j]
            hn = A[i-1][j] if i-1 >= 0 else 0
            area += max(0, h - hn)
            hn = A[i+1][j] if i+1 < H else 0
            area += max(0, h - hn)
            hn = A[i][j-1] if j-1 >= 0 else 0
            area += max(0, h - hn)
            hn = A[i][j+1] if j+1 < W else 0
            area += max(0, h - hn)
        
    return area
