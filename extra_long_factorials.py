# Exercise: Extra Long Factorials
# URL: https://www.hackerrank.com/challenges/extra-long-factorials/problem?isFullScreen=true
# Description: Calculate and print the factorial of a given integer n

def extraLongFactorials(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    print(factorial)
