import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('G.txt')

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[-1] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    if x == 0 and y == 0:
        return 1

    if visited[x][y] == -1:
        # 방문 표시
        visited[x][y] = 0
        for idx in range(4):
            new_x, new_y = x + dx[idx], y + dy[idx]    
            if 0 <= new_x < n and 0 <= new_y < m and graph[new_x][new_y] > graph[x][y]:
                visited[x][y] += dfs(new_x, new_y)

    return visited[x][y]


dfs(n - 1, m - 1)

print(visited[n - 1][m - 1])