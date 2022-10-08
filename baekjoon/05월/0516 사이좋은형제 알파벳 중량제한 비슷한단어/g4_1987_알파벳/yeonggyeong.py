from collections import deque
import sys
sys.stdin = open('G.txt')

R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]

answer = matrix[0][0]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    global answer
    q = deque()
    q.append((x, y, matrix[x][y]))

    while q:
        x, y, alph = q.pop()
        for idx in range(4):
            new_x, new_y = x + dx[idx], y + dy[idx]
            if 0 <= new_x < R and 0 <= new_y < C and matrix[new_x][new_y] not in alph:
                q.append((new_x, new_y, alph + matrix[new_x][new_y]))
                if len(answer) <= len(alph + matrix[new_x][new_y]):
                    answer = alph + matrix[new_x][new_y]


dfs(0, 0)
print(len(answer))