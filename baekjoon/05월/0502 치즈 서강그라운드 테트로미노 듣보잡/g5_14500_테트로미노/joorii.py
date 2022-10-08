import sys
sys.stdin = open('M.txt')


def dfs(r, c, idx, total):
    global ans
    # 상 하 좌 우
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))

    if ans >= total + max_val * (3 - idx):          # 가지치기
        return
    if idx == 3:                                    # 깊이 3까지 탐색 후
        ans = max(ans, total)
        return
    for k in range(4):
        nr, nc = r + d[k][0], c + d[k][1]
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            if idx == 1:                # ㅗ, ㅜ, ㅏ, ㅓ
                visited[nr][nc] = 1
                dfs(r, c, idx + 1, total + matrix[nr][nc])
                visited[nr][nc] = 0
            visited[nr][nc] = 1
            dfs(nr, nc, idx + 1, total + matrix[nr][nc])
            visited[nr][nc] = 0


# 세로 크기 N, 가로 크기 M
N, M = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
ans = 0
max_val = max(map(max, matrix))

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 0, matrix[i][j])
        visited[i][j] = 0

print(ans)
