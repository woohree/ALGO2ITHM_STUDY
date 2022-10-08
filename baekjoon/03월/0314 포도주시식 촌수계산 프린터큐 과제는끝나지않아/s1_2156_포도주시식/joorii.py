import sys
sys.stdin = open('M.txt')


def max_wine():

    dp[0] = wines[0]
    # n = 2일 때,
    if n > 1:
        dp[1] = wines[0] + wines[1]
    # n > 2일 때,
    if n > 2:
        # 0번째와 2번째 [o,x,o]
        temp_1 = dp[0] + wines[2]
        # 1번쨰와 2번째 [x,o,o]
        temp_2 = wines[1] + wines[2]
        if temp_1 > temp_2:
            dp[2] = temp_1
        else:
            dp[2] = temp_2

        # 0번째와 1번째 [o,o,x]
        if dp[2] < dp[1]:
            dp[2] = dp[1]

        # n > 3일 때
        for i in range(3, n):
            # [x,o,o]
            temp_1 = dp[i - 3] + wines[i - 1] + wines[i]
            # [o,x,o]
            temp_2 = dp[i - 2] + wines[i]

            if temp_1 > temp_2:
                dp[i] = temp_1
            else:
                dp[i] = temp_2

            # [o,o,x]
            if dp[i] < dp[i - 1]:
                dp[i] = dp[i - 1]

    return dp[n - 1]


n = int(input())
wines = [int(input()) for _ in range(n)]

dp = [0] * n

print(max_wine())
