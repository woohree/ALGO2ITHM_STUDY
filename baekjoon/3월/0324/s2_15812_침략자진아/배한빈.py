import sys
sys.stdin = open('B.txt')

import itertools
import collections

N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]

# 값이 0인 2개의 좌표 조합 만들기
coords = [(col, row) for col in range(N) for row in range(M) if int(matrix[col][row]) == 0]
comb = list(itertools.combinations(coords, 2))

# 마을의 개수 세기
village = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == '1':
            village += 1

# bfs 이용해서 max 값 찾기
moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
my_min = N * M
for c in comb:
    visited = [[0] * M for _ in range(N)]
    visited[c[0][0]][c[0][1]] = 1
    visited[c[1][0]][c[1][1]] = 1

    count = 0
    v = village

    queue1, queue2 = collections.deque([]), collections.deque([])
    queue1.append(c[0])
    queue2.append(c[1])
    while 1:
        for _ in range(len(queue1)):
            first = queue1.popleft()
            for move in moves:
                if 0 <= first[0] + move[0] < N and 0 <= first[1] + move[1] < M:
                    if visited[first[0] + move[0]][first[1] + move[1]] == 0:
                        queue1.append([first[0] + move[0], first[1] + move[1]])
                        visited[first[0] + move[0]][first[1] + move[1]] = 1
                        if matrix[first[0] + move[0]][first[1] + move[1]] == '1':
                            v -= 1

        for _ in range(len(queue2)):
            second = queue2.popleft()
            for move in moves:
                if 0 <= second[0] + move[0] < N and 0 <= second[1] + move[1] < M:
                    if visited[second[0] + move[0]][second[1] + move[1]] == 0:
                        queue2.append([second[0] + move[0], second[1] + move[1]])
                        visited[second[0] + move[0]][second[1] + move[1]] = 1
                        if matrix[second[0] + move[0]][second[1] + move[1]] == '1':
                            v -= 1
        count += 1
        if v <= 0:
            if my_min > count:
                my_min = count
            break

# 출력
print(my_min)
