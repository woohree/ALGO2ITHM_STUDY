import sys
sys.stdin = open('M.txt')


def cases(n):
    dp = [0] * 12       # n은 양수이며 11보다 작다.
    dp[1], dp[2], dp[3] = 1, 2, 4
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]


T = int(input())

for tc in range(T):
    n = int(input())
    print(cases(n))
