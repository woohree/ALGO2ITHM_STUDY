import sys
from collections import deque
sys.stdin = open('B.txt')


def separate_iceberg():
    first_iceberg = [iceberg[0]]
    q = deque()
    q.append(iceberg[0])
    while q:
        r, c = q.popleft()
        for d in directions:
            if matrix[r + d[0]][c + d[1]] != 0 and (r + d[0], c + d[1]) not in first_iceberg:
                q.append((r + d[0], c + d[1]))
                first_iceberg.append((r + d[0], c + d[1]))
    if len(first_iceberg) == len(iceberg):
        return 0
    else:
        return 1


def melt_iceberg(y):
    while iceberg:
        temp = []
        for _ in range(len(iceberg)):
            ice = iceberg.popleft()
            count = 0
            for d in directions:
                if matrix[ice[0] + d[0]][ice[1] + d[1]] == 0:
                    count += 1
            temp.append((ice, count))
        for ice, count in temp:
            matrix[ice[0]][ice[1]] -= count
            if matrix[ice[0]][ice[1]] < 0:
                matrix[ice[0]][ice[1]] = 0
            elif matrix[ice[0]][ice[1]] > 0:
                iceberg.append(ice)
        y += 1
        if iceberg and separate_iceberg():
            return y
    return 0


N, M = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

iceberg = []
for i in range(1, N-1):
    for j in range(1, M-1):
        if matrix[i][j] != 0:
            icebergs.append((i, j))

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
print(melt_iceberg(-1))
