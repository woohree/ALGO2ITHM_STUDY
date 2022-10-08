import sys
from collections import deque
sys.stdin = open('B.txt')
# 16분


def bfs(row, col):
    count = 1
    q = deque()
    q.append((row, col))
    while q:
        r, c = q.popleft()
        for move in moves:
            next_r, next_c = r + move[0], c + move[1]
            if 0 <= next_r < N and 0 <= next_c < N:
                if matrix[next_r][next_c] == '1' and visited[next_r][next_c] == 0:
                    q.append((next_r, next_c))
                    visited[next_r][next_c] = 1
                    count += 1
    return count


N = int(sys.stdin.readline().rstrip())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
visited = [[0 for _ in range(N)] for _ in range(N)]
result = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == '1' and visited[i][j] == 0:
            visited[i][j] = 1
            result.append(bfs(i, j))

r = len(result)
print(r)
result.sort()
for k in range(r):
    print(result[k])
