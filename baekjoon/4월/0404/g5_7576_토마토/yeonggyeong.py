from collections import deque
import sys
sys.stdin = open('G.txt')


def bfs():
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y = queue.popleft()

        for idx in range(4):
            new_x, new_y = x + dx[idx], y + dy[idx]
            # 익지 않은 토마토일때
            if 0 <= new_x < N and 0 <= new_y < M and not matrix[new_x][new_y]:
                # 해당 위치에 도달하는 시간
                matrix[new_x][new_y] = matrix[x][y] + 1
                queue.append([new_x, new_y])


M, N = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

queue = deque()

# 익은 토마토 위치 찾기
for row in range(N):
    for col in range(M):
        if matrix[row][col] == 1:
            queue.append([row, col])

# print(matrix)
bfs()
# print(matrix)
answer = 0
for row in range(N):
    for col in range(M):
        # 익지 않은 토마토가 존재한다면
        if matrix[row][col] == 0:
            print(-1)
            exit(0)
    answer = max(answer, max(matrix[row]))
print(answer - 1)