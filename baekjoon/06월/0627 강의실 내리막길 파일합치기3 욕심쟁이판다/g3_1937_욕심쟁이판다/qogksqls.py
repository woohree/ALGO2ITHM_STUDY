import sys
sys.stdin = open('B.txt')


def dfs(r, c):
    if dp[r][c] != 0:
        return dp[r][c]
    max_temp = 0
    for move in moves:
        dr, dc = move[0] + r, move[1] + c
        if 0 <= dr < n and 0 <= dc < n and matrix[r][c] < matrix[dr][dc]:
            max_temp = max(max_temp, dfs(dr, dc))
    if not max_temp:
        dp[r][c] = 1
    dp[r][c] = max_temp + 1
    print(dp)
    return dp[r][c]


n = int(sys.stdin.readline().rstrip())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
for i in range(n):
    for j in range(n):
        dfs(i, j)
answer = 0
for i in range(n):
    answer = max(answer, max(dp[i]))
print(answer)
