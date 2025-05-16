# Exercise: Encryption
# URL: https://www.hackerrank.com/challenges/encryption/problem?isFullScreen=true
# Description:
# Encrypt a string by removing spaces, arranging characters in a grid, 
# and reading column-wise with spaces between columns

import math

def encryption(s):
    s = s.replace(" ", "")
    L = len(s)
    rows = math.floor(math.sqrt(L))
    cols = math.ceil(math.sqrt(L))
    if rows * cols < L:
        rows += 1

    result = []
    for c in range(cols):
        word = ''.join(s[r * cols + c] for r in range(rows) if r * cols + c < L)
        result.append(word)
    
    return ' '.join(result)







