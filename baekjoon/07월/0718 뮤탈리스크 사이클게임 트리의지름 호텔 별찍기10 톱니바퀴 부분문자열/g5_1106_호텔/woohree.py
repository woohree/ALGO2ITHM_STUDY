import sys
sys.stdin = open('W.txt')


C, N = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(N)]
inf = float('inf')
dp = [inf] * (C+100)
dp[0] = 0
for cost, customer in cities:
    for i in range(customer, C+100):
        dp[i] = min(dp[i], dp[i-customer]+cost)
ans = min(dp[C:])
print(ans)
print(dp)