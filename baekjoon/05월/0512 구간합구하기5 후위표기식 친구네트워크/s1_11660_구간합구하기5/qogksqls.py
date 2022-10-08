import sys
sys.stdin = open('B.txt')

N, M = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = matrix[0][0]
for i in range(N):
    for j in range(N):
        if 0 <= i-1 < N:
            if j == 0:
                dp[i][j] += dp[i-1][0] + matrix[i][0]
            else:
                dp[i][j] += dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i][j]
        elif 1 <= j < N:
            dp[i][j] += dp[i][j-1] + matrix[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    minus = 0
    if x1 != 1:
        minus += dp[x1-2][y2-1]
    if y1 != 1:
        minus += dp[x2-1][y1-2]
    if x1 != 1 and y1 != 1:
        minus -= dp[x1-2][y1-2]

    print(dp[x2-1][y2-1] - minus)
