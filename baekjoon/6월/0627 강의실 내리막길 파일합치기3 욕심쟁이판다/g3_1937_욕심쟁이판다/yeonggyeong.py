import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('G.txt')

input = sys.stdin.readline

n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1]*n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
result = 0


def dfs(x, y):

    if dp[x][y] == -1:
        dp[x][y] = 0

        for idx in range(4):
            new_x, new_y = x + dx[idx], y + dy[idx]    
            if 0 <= new_x < n and 0 <= new_y < n and matrix[new_x][new_y] > matrix[x][y]:
                dp[x][y] = max(dp[x][y], dfs(new_x, new_y))

    return dp[x][y] + 1


for r in range(n):
    for c in range(n):
        result = max(result, dfs(r, c))
print(result)