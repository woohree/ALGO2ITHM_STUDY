import sys
sys.stdin = open('W.txt')


def dfs(r, c, idx):
    global cnt
    if visited[r][c] != -1:                                     # 이미 지난 지점이면 일단 컷!
        if visited[r][c] == idx:                                # 시작지점에 다시 도달했을 때만 +1
            cnt += 1
        return

    visited[r][c] = idx                                         # 방문체크
    d = mat[r][c]
    new_r, new_c = r + dirs[d][0], c + dirs[d][1]
    if 0 <= new_r < N and 0 <= new_c < M:
        dfs(new_r, new_c, idx)


N, M = map(int, input().split())
mat = [list(input()) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]
dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}   # 방향설정 딕셔너리
cnt = idx = 0
for i in range(N):
    for j in range(M):
        dfs(i, j, idx)
        idx += 1
print(cnt)