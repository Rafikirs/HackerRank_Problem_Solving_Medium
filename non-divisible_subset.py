# Exercise: Non-Divisible Subset
# URL: https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true
# Description: 
# Find the largest subset of distinct integers where the sum of any two numbers 
# is not divisible by a given integer k

def nonDivisibleSubset(k, S):
    remainder_counts = [0] * k
    for num in S:
        remainder_counts[num % k] += 1

    count = min(remainder_counts[0], 1)

    for i in range(1, (k // 2) + 1):
        if i != k - i:
            count += max(remainder_counts[i], remainder_counts[k - i])
        else:
            count += min(remainder_counts[i], 1)

    return count







