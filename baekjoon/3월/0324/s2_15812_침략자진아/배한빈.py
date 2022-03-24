import sys
sys.stdin = open('B.txt')

import itertools
import collections

N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]

# 값이 0인 2개의 좌표 조합 만들기
coords = [(col, row) for col in range(N) for row in range(N) if int(matrix[col][row]) == 0]
comb = list(itertools.combinations(coords, 2))

# 마을의 개수 세기
village = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == '1':
            village += 1

# bfs 이용해서 max 값 찾기
visited = [[0] * M for _ in range(N)]
moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
my_max = N + M
for c in comb:
    count = 0
    queue = collections.deque([])
    queue.append(c[0])
    queue.append(c[1])
    while queue:
        first = queue.popleft()
        visited[first[0]][first[1]] = 1
        for move in moves:
            if 0 <= first[0] + move[0] < N and 0 <= first[1] + move[1] < N:
                if visited[first[0] + move[0]][first[1] + move[1]] == 0:
                    if matrix[first[0] + move[0]][first[1] + move[1]] == 1:
                    #
                    # queue.append([first[0] + move[0], first[1] + move[1]])

        second = queue.popleft()
        visited[second[0]][second[1]] = 1
        for move in moves:
            if 0 <= second[0] + move[0] < N and 0 <= second[1] + move[1] < N:
                if visited[second[0] + move[0]][second[1] + move[1]] == 0:
                    queue.append([second[0] + move[0], second[1] + move[1]])

    if my_max > count:
        my_max = count

# 출력
print(my_max)
