import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('L.txt')


def dfs(r, c, color):
    global cnt_disabled, cnt_common

    if len(color) == 1:                         # R, G, B 하나만 세는 경우
        visited[r][c] = 1
        for move in moves:
            newr, newc = r + move[0], c + move[1]
            if 0 <= newr < N and 0 <= newc < N and not visited[newr][newc] and mat[newr][newc] == color:
                dfs(newr, newc, color)

    else:                                       # R, G 두개 세는 경우(적록색약)
        visited2[r][c] = 1
        for move in moves:
            newr, newc = r + move[0], c + move[1]
            if 0 <= newr < N and 0 <= newc < N and not visited2[newr][newc] and mat[newr][newc] in color:
                dfs(newr, newc, color)


N = int(sys.stdin.readline().rstrip())
mat = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
visited2 = [[0]*N for _ in range(N)]
moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
cnt_common = cnt_disabled = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            if mat[i][j] == 'R':
                dfs(i, j, 'R')
                cnt_common += 1
            elif mat[i][j] == 'G':
                dfs(i, j, 'G')
                cnt_common += 1
            else:
                dfs(i, j, 'B')
                cnt_common += 1
                cnt_disabled += 1
        if not visited2[i][j]:
            if mat[i][j] == 'R' or mat[i][j] == 'G':
                dfs(i, j, ('R', 'G'))
                cnt_disabled += 1

print(cnt_common, cnt_disabled)
