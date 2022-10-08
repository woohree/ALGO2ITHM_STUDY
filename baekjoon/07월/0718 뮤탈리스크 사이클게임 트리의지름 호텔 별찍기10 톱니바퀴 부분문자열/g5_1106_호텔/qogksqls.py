import sys
sys.stdin = open('B.txt')

'''
30분.. 근데 무의미
1. 잘 생각이 안나서 구글링 함..
2. 근데 또 이해 안되서 그냥 설명 들을게요
'''

C, N = map(int, sys.stdin.readline().rstrip().split())
info = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]  # 비용, 고객 수

INF = float(1e9)
dp = [INF] * (C+100)
dp[0] = 0
for cost, cus in info:
    for i in range(cus, C + 100):
        dp[i] = min(dp[i], dp[i - cus] + cost)

print(min(dp[C:]))
