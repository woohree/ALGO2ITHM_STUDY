import sys
sys.stdin = open('G.txt ')


def dfs(x, y, block_sum, block_cnt):
    global max_value

    if block_cnt == 4:
        max_value = max(max_value, block_sum)
        return 
    
    for idx in range(4):
        new_x, new_y = x + dx[idx], y + dy[idx]
        if 0 <= new_x < N and 0 <= new_y < M and not visited[new_x][new_y]:
            visited[new_x][new_y] = 1
            dfs(new_x, new_y, block_sum+matrix[new_x][new_y], block_cnt+1)
            visited[new_x][new_y] = 0


N, M = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

max_value = float('-inf')

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for row in range(N):
    for col in range(M):
        visited[row][col] = 1
        dfs(row, col, 0, 0)
        visited[row][col] = 0
print(max_value)