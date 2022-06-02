import copy
import sys
sys.stdin = open('M.txt')

n = int(sys.stdin.readline())
tri = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = copy.deepcopy(tri)

for i in range(n - 1):
    for j in range(i + 1):
        dp[i + 1][j] = max(dp[i + 1][j], tri[i + 1][j] + dp[i][j])
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], tri[i + 1][j + 1] + dp[i][j])

print(max(dp[n - 1]))
