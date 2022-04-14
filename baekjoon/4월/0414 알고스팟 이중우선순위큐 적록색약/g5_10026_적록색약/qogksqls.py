import sys
from collections import deque
sys.stdin = open('B.txt')

# 30m
# BFS 로 풀이
# red 영역, green 영역, blue 영역,
# 그리고 적록색맹의 경우 빨강과 초록을 같이 세야 하기 때문에 함수가 총 4개 나왔다.


def red():
    while queue:
        for _ in range(len(queue)):
            temp = queue.popleft()
            for move in moves:
                row = temp[0] + move[0]
                col = temp[1] + move[1]
                if 0 <= row < N and 0 <= col < N:
                    if visited[row][col] == 0 and matrix[row][col] == 'R':
                        queue.append((row, col))
                        visited[row][col] = 1
    return


def green():
    while queue:
        for _ in range(len(queue)):
            temp = queue.popleft()
            for move in moves:
                row = temp[0] + move[0]
                col = temp[1] + move[1]
                if 0 <= row < N and 0 <= col < N:
                    if visited[row][col] == 0 and matrix[row][col] == 'G':
                        queue.append((row, col))
                        visited[row][col] = 1
    return


def blue():
    while queue:
        for _ in range(len(queue)):
            temp = queue.popleft()
            for move in moves:
                row = temp[0] + move[0]
                col = temp[1] + move[1]
                if 0 <= row < N and 0 <= col < N:
                    if visited[row][col] == 0 and matrix[row][col] == 'B':
                        queue.append((row, col))
                        visited[row][col] = 1
    return


def red_green():
    while queue:
        for _ in range(len(queue)):
            temp = queue.popleft()
            for move in moves:
                row = temp[0] + move[0]
                col = temp[1] + move[1]
                if 0 <= row < N and 0 <= col < N:
                    if visited[row][col] == 0 and (matrix[row][col] == 'R' or matrix[row][col] == 'G'):
                        queue.append((row, col))
                        visited[row][col] = 1
    return


N = int(input())
matrix = [list(input()) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]

RGB = [0, 0, 0]  # 영역 개수 카운트하는 리스트
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            if matrix[i][j] == 'R':
                visited[i][j] = 1
                queue = deque()
                queue.append((i, j))
                red()
                RGB[0] += 1
            if matrix[i][j] == 'G':
                visited[i][j] = 1
                queue = deque()
                queue.append((i, j))
                green()
                RGB[1] += 1
            if matrix[i][j] == 'B':
                visited[i][j] = 1
                queue = deque()
                queue.append((i, j))
                blue()
                RGB[2] += 1

RG_B = [0, RGB[2]]  # blue 영역의 개수는 정상인과 적록색맹 둘 다 같다.
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            if matrix[i][j] == 'R' or matrix[i][j] == 'G':
                visited[i][j] = 1
                queue = deque()
                queue.append((i, j))
                red_green()
                RG_B[0] += 1

print(sum(RGB), sum(RG_B))
