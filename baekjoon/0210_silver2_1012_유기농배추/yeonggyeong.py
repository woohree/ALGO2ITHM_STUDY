import sys
sys.stdin = open('input.txt')


def dfs(row, col):
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for idx in range(4):
        row, col = row+dx[idx], col+dy[idx]

        if 0 <= row < N and 0 <= col < M and matrix[row][col] != 0:
            matrix[row][col] = 0
            dfs(row, col)
        row, col = row-dx[idx], col-dy[idx]


T = int(input())

for tc in range(T):
    M, N, K = map(int, input().split())

    matrix = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1
    cnt = 0
    for x in range(N):
        for y in range(M):
            if matrix[x][y] != 0:
                cnt += 1
                matrix[x][y] = 0
                dfs(x, y)

    print(cnt)