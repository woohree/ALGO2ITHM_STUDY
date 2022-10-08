import sys
from collections import deque

'''
1. 한 마디로 어느 한 지점에서 가장 멀리 갈 수 있는 곳의 최단거리 구하기
2. bfs 사용
'''

sys.stdin = open('B.txt')

N, M = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

my_max = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'L':
            visited = [[0] * M for _ in range(N)]
            q = deque()
            q.append((i, j))
            visited[i][j] = 1
            time = 0
            while q:
                for _ in range(len(q)):
                    now = q.popleft()
                    for move in moves:
                        r = now[0] + move[0]
                        c = now[1] + move[1]
                        if 0 <= r < N and 0 <= c < M:
                            if visited[r][c] == 0 and matrix[r][c] == 'L':
                                visited[r][c] = 1
                                q.append((r, c))
                if q:
                    time += 1
            my_max = max(my_max, time)
print(my_max)
