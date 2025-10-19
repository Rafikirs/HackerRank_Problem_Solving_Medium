# Exercise: The Grid Search
# URL: https://www.hackerrank.com/challenges/the-grid-search/problem?isFullScreen=true
# Description: Searching whether a pattern is present within a grid or not

def gridSearch(G, P):
    P_width = len(P[0])
    G_width = len(G[0])
    for i in range(len(G) - len(P) + 1):
        if P[0] in G[i]:
            good_index = G[i].index(P[0])   
            for k in range(good_index, G_width-P_width+1):
                if all(G[i+j][k:k+P_width] == P[j] for j in range(len(P))):
                    return "YES"
    return "NO"
