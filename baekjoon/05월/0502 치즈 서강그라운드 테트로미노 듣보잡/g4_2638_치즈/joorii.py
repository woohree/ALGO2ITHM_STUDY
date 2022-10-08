from pprint import pprint
from collections import deque
import sys
sys.stdin = open('M.txt')


def melt():
    drc = ((-1, 0), (1, 0), (0, -1), (0, 1))
    time = 0
    while 1:
        # bfs 치즈 외부, 내부 구하기
        visited = [[0] * M for _ in range(N)]
        nexts = deque()
        nexts.append((0, 0))
        visited[0][0] = 1

        while nexts:
            cur_r, cur_c = nexts.popleft()
            for d in drc:
                next_r, next_c = cur_r + d[0], cur_c + d[1]
                if 0 <= next_r < N and 0 <= next_c < M:
                    if not visited[next_r][next_c] and matrix[next_r][next_c] != 1:      # 방문 안 한 곳이고, 치즈가 아닐 때
                        matrix[next_r][next_c] = 3                      # 치즈 외부는 3으로 변경
                        nexts.append((next_r, next_c))
                        visited[next_r][next_c] = 1

        # 녹을 치즈 구하기
        time += 1
        inner_cheeses = []
        outer_cheeses = []
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 1:                   # 치즈 일 때
                    temp_cnt = 0
                    for d in drc:                       # 사방 탐색
                        nr, nc = i + d[0], j + d[1]
                        if matrix[nr][nc] == 3:         # 외부 공기와 맞닿아 있을 때
                            temp_cnt += 1
                            if temp_cnt >= 2:           # 2면 이상 맞닿아 있을 때
                                outer_cheeses.append((i, j))
                                break
                    else:                               # 사방 탐색 후 2면 이상 외부와 맞닿아 있지 않을 때
                        inner_cheeses.append((i, j))

        if not inner_cheeses:
            return time

        for cheese in outer_cheeses:                    # 녹은 치즈 표시하기
            matrix[cheese[0]][cheese[1]] = 3


# 세로 길이 N, 가로 길이 M
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
print(melt())
