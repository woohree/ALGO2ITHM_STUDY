import sys
sys.stdin = open('B.txt')

from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

out_air_zone = [[0] * M for _ in range(N)]
out_air_zone[0][0] = 1
air_zone = deque()
air_zone.append((0, 0))
time = 0
next_air_zone = []
while 1:
    if next_air_zone:
        air_zone.extend(next_air_zone)
    while air_zone:
        current = air_zone.popleft()
        for i in range(4):
            next_y = current[0] + dy[i]
            next_x = current[1] + dx[i]
            if 0 <= next_x < M and 0 <= next_y < N:
                if out_air_zone[next_y][next_x] != 1 and matrix[next_y][next_x] == 0:
                    air_zone.append((next_y, next_x))
                    out_air_zone[next_y][next_x] = 1
    check = 0
    for row in out_air_zone:
        if 0 in row:
            check += 1
            break
    if check == 0:
        break

    next_air_zone = []
    for row in range(N):
        for col in range(M):
            if out_air_zone[row][col] == 0:
                count = 0
                for j in range(4):
                    next_row = row + dy[j]
                    next_col = col + dx[j]
                    if out_air_zone[next_row][next_col] == 1:
                        count += 1
                        if count == 2:
                            break
                if count == 2:
                    next_air_zone.append((row, col))
    for naz in next_air_zone:
        out_air_zone[naz[0]][naz[1]] = 1
    time += 1

print(time)
