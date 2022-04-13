import sys
sys.stdin = open('M.txt')


# 적록색약이 아닌경우
def rgb_dfs(r, c):
    # 상 우 하 좌
    d = ((-1, 0), (0, 1), (1, 0), (0, -1))
    rgb_visited[r][c] = 1
    for i in range(4):
        nr, nc = r + d[i][0], c + d[i][1]
        if 0 <= nr < N and 0 <= nc < N and not rgb_visited[nr][nc] and matrix[r][c] == matrix[nr][nc]:
            rgb_dfs(nr, nc)
    else:
        return 1


# 적록색약인 경우
def rb_dfs(r, c):
    # 상 우 하 좌
    d = ((-1, 0), (0, 1), (1, 0), (0, -1))
    rb_visited[r][c] = 1
    for i in range(4):
        nr, nc = r + d[i][0], c + d[i][1]
        if 0 <= nr < N and 0 <= nc < N and not rb_visited[nr][nc]:
            if matrix[r][c] in ['R', 'G'] and matrix[nr][nc] in ['R', 'G']:
                rb_dfs(nr, nc)
            elif matrix[r][c] == 'B' and matrix[nr][nc] == 'B':
                rb_dfs(nr, nc)
    else:
        return 1


N = int(input())
matrix = [list(map(str, input())) for _ in range(N)]
colorful = colorless = 0
rgb_visited = [[0 for _ in range(N)] for _ in range(N)]
rb_visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not rgb_visited[i][j]:           # 적록색약이 아닌경우
            colorful += rgb_dfs(i, j)
        if not rb_visited[i][j]:            # 적록색약인 경우
            colorless += rb_dfs(i, j)

print(colorful, colorless)
