import sys, copy
from itertools import combinations
from collections import deque

sys.stdin = open('B.txt')

N, M = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

locations = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2:
            locations.append((i, j))

moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
comb = list(combinations(locations, M))
my_min, flag = N * N, 0
for c in comb:
    visited = [[0] * N for _ in range(N)]
    temp = copy.deepcopy(matrix)
    q = deque(c)
    time, ans = 0, 0
    for a in q:
        visited[a[0]][a[1]] = 1
        temp[a[0]][a[1]] = 2
    while q:
        time += 1
        for _ in range(len(q)):
            now = q.popleft()
            for move in moves:
                r = now[0] + move[0]
                c = now[1] + move[1]
                if 0 <= r < N and 0 <= c < N:
                    if visited[r][c] == 0 and temp[r][c] == 2:
                        visited[r][c] = 1
                        q.append((r, c))
                    elif visited[r][c] == 0 and temp[r][c] != 1:
                        ans = time
                        visited[r][c] = 1
                        temp[r][c] = time
                        q.append((r, c))
    no = 1
    for row in temp:
        if 0 in row:
            no = 0
            break
    if no:
        my_min = min(my_min, ans)
if my_min == N * N:
    print(-1)
else:
    print(my_min)
