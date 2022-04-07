import sys
sys.stdin = open('B.txt')

from collections import deque

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 1 <= h <= 100
# 높이의 최대값 구하기
max_height = 0
for a in range(N):
    for b in range(N):
        if max_height < matrix[a][b]:
            max_height = matrix[a][b]

moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
rain = 0
max_safe_zone = 0
while rain <= max_height:
    safe_zone = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if rain < matrix[i][j] and visited[i][j] == 0:
                # bfs
                queue = deque()  # 질문: queue = deque(((i, j))) => i=0,j=0 일 때 합쳐져서 0 이라 뜸
                queue.append((i, j))
                visited[i][j] = 1
                while queue:
                    temp = queue.popleft()  # temp = 0으로 됨
                    for move in moves:
                        # N x N 벗어나지 않도록 범위 설정
                        if 0 <= temp[0] + move[0] < N and 0 <= temp[1] + move[1] < N:
                            # visited 가 0인지 체크, rain 보다 높은지 체크
                            if visited[temp[0] + move[0]][temp[1] + move[1]] == 0 and matrix[temp[0] + move[0]][temp[1] + move[1]] > rain:
                                queue.append([temp[0] + move[0], temp[1] + move[1]])
                                visited[temp[0] + move[0]][temp[1] + move[1]] = 1
                safe_zone += 1
    # 최대값 구하기
    if max_safe_zone < safe_zone:
        max_safe_zone = safe_zone
    rain += 1

print(max_safe_zone)
