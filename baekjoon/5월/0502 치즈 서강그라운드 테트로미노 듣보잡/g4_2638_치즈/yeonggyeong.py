import sys
from collections import deque
sys.stdin = open('G.txt')


def solution():
    queue = deque()
    # 가장자리는 치즈가 없으므로 항상 0, 0 시작
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        for idx in range(4):
            new_x, new_y = x + dx[idx], y + dy[idx]
            if 0 <= new_x < N and 0 <= new_y < M:
                # 외부 공기로 바꿔주기
                if not matrix[new_x][new_y]:
                    matrix[new_x][new_y] = -1
                    queue.append((new_x, new_y))
                # 외부 공기에 접촉된 선분 추가
                elif matrix[new_x][new_y] >= 1:
                    matrix[new_x][new_y] += 1
    
    for row in range(N):
        for col in range(M):
            # 3이상이면 접촉 선분이 2개 이상 / 외부 공기는 다시 처음처럼 초기화
            if matrix[row][col] == -1 or matrix[row][col] >= 3:
                matrix[row][col] = 0
            # 치즈는 1로 변경
            elif matrix[row][col]:
                matrix[row][col] = 1


N, M = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0
# 모든 치즈가 녹기전까지 반복
while sum([sum(i) for i in matrix]) != 0:
    solution()
    time += 1
print(time)