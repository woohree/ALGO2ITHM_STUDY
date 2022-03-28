# 1,2,3의 합만으로 나타내는 방법의 수

# 6:00

import sys
sys.stdin = open('B.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())

    dp = [[1, 0, 0], [1, 1, 0], [1, 1, 1]]

    if n > 3:
        i = 4
        while i <= n:
            temp = []
            temp.append(dp[i-2][0])
            temp.append(dp[i-3][0] + dp[i-3][1])
            temp.append(dp[i-4][0] + dp[i-4][1] + dp[i-4][2])
            dp.append(temp)
            i += 1
        print(sum(dp[n-1]))
    else:
        print(sum(dp[n-1]))
