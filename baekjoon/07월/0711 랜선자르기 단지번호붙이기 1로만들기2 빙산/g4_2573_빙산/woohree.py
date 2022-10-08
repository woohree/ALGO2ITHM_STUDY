import sys
sys.setrecursionlimit(10**4)
sys.stdin = open('L.txt')


def dfs(r, c):
    cnt = 0
    for move in moves:
        new_r, new_c = r + move[0], c + move[1]
        if 0 <= new_r < N and 0 <= new_c < M and visited[new_r][new_c] == -1 and mat[new_r][new_c] > 0:
            visited[new_r][new_c] = 0
            dfs(new_r, new_c)
        if 0 <= new_r < N and 0 <= new_c < M and mat[new_r][new_c] <= 0:
            cnt += 1
    visited[r][c] = cnt
    # temp.setdefault((r, c), 0)
    # temp[(r, c)] = cnt


N, M = map(int, input().split())
mat = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
moves = ((1, 0), (-1, 0), (0, -1), (0, 1))
ans = -1

while 1:
    ans += 1
    trigger = 0
    visited = [[-1]*M for _ in range(N)]
    # temp = {}
    for i in range(N):
        for j in range(M):
            if visited[i][j] == -1 and mat[i][j] > 0:
                trigger += 1
                if trigger > 1:
                    break
                visited[i][j] = 0
                dfs(i, j)
                # for (r, c), cnt in temp.items():
                #     mat[r][c] -= cnt
                for i in range(N):
                    for j in range(M):
                        if visited[i][j] != -1:
                            mat[i][j] -= visited[i][j]
        if trigger > 1:
            break
    if trigger > 1:
        break
print(ans)