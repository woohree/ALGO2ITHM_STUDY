import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('B.txt')

'''
1. dfs, bfs 모두 시간초과
2. dp, 메모이제이션...
'''


def dfs(r, c):
    if dp[r][c] != -1:
        return dp[r][c]
    temp = 0
    for move in moves:
        dr, dc = move[0] + r, move[1] + c
        if 0 <= dr < H and 0 <= dc < W and matrix[r][c] > matrix[dr][dc]:
            temp += dfs(dr, dc)
    dp[r][c] = temp
    return dp[r][c]


H, W = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(H)]
dp = [[-1] * W for _ in range(H)]
dp[-1][-1] = 1

moves = ((1, 0), (0, 1), (-1, 0), (0, -1))

print(dfs(0, 0))
