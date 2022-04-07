import sys
sys.stdin = open('M.txt')


# 중량이 높아지고, 선명도의 값이 낮아지는 부분열 중 최장의 것의 길이
def func():
    dp = [1 for _ in range(N)]
    for n in range(N):
        for i in range(n):
            if diamonds[i][0] < diamonds[n][0] and diamonds[i][1] > diamonds[n][1]:
                dp[n] = max(dp[n], dp[i] + 1)
    return max(dp)


T = int(input())

for _ in range(T):
    N = int(input())
    # 무게 w, 선명도 c
    diamonds = [list(map(float, input().split())) for _ in range(N)]
    # diamonds.sort(key=lambda x: x[0])
    print(func())
