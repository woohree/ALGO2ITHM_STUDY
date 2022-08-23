import sys
from itertools import combinations
from collections import deque

sys.stdin = open('B.txt')

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

locations = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2:
            locations.append((i, j))


moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
comb = list(combinations(locations, 3))
my_max = 0
for c in comb:
    visited = [[0] * N for _ in range(N)]
    q = deque(c)
    time = 0
    while q:
        for _ in range(len(q)):
            now = q.popleft()
            visited[now[0]][now[1]] = 1
            for move in moves:
                r = now[0] + move[0]
                c = now[1] + move[1]
                if 0 <= r < N and 0 <= c < M:
                    if visited[r][c] == 0 and matrix[r][c] == 0:
                        visited[r][c] = 1
                        matrix[r][c] = time
                        q.append((r, c))
        time += 1
    my_max = max(my_max, time)
print(my_max)
