# 1. bfs로 풀면 방문이 겹치는 경우가 생길거같아 dfs로 풀고자 함
# 2. 0-1bfs 해보려 했지만 포기
# 3. bfs, `appendleft` 활용
import sys
sys.stdin = open('B.txt')

from collections import deque


def bfs():
    while queue:
        temp = queue.popleft()
        for move in moves:
            next_row = temp[0] + move[0]
            next_col = temp[1] + move[1]
            if 0 <= next_row < N and 0 <= next_col < M:
                if visited[next_row][next_col] == -1:
                    # 벽(1)을 만나면 append해주고
                    if matrix[next_row][next_col] == '1':
                        queue.append((next_row, next_col))
                        visited[next_row][next_col] = visited[temp[0]][temp[1]] + 1

                    # 통로(0)일 경우를 appendleft 해줘 먼저 계산 되도록 함
                    # next 값을 next 이전 값으로 바꿔줘 누적 합을 계산
                    elif matrix[next_row][next_col] == '0':
                        queue.appendleft((next_row, next_col))
                        visited[next_row][next_col] = visited[temp[0]][temp[1]]


M, N = map(int, input().split())
matrix = [list(input()) for _ in range(N)]

moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
visited = [[-1] * M for _ in range(N)]
visited[0][0] = 0

queue = deque()
queue.append((0, 0))
bfs()

# visited 의 최우하단 값을 출력
print(visited[N - 1][M - 1])

'''
def dfs(row, col, wall):
    global my_min

    if my_min <= wall:
        return

    if row == N-1 and col == M-1:
        my_min = min(my_min, wall)
        return

    for move in moves:
        next_row = row + move[0]
        next_col = col + move[1]
        if 0 <= next_row < N and 0 <= next_col < M:
            if visited[next_row][next_col] == 0:
                visited[next_row][next_col] = 1
                if matrix[next_row][next_col] == '1':
                    dfs(next_row, next_col, wall + 1)
                elif matrix[next_row][next_col] == '0':
                    dfs(next_row, next_col, wall)
                visited[next_row][next_col] = 0


M, N = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]

visited[0][0] = 1
my_min = N * M
dfs(0, 0, 0)

print(my_min)
'''