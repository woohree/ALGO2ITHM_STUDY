# baekjoon 1012 유기농배추

# 테스트 케이스 T 
# 배추밭 가로길이 M / 배추밭 세로길이 N / 배추 위치 개수 K
# 배추의 위치 X, Y 

import sys
sys.stdin = open('input.txt')


def find_warm(x, y):
    # 배추밭 범위를 벗어났을 때
    if x < 0 or y < 0 or x >= N or y >= M:
        return

    # 배추밭에 배추가 없을 때
    if cabbage_list[x][y] == 0:
        return

    # 탐색한 배추밭은 0으로 변경
    cabbage_list[x][y] = 0

    # 상하좌우 사방향 탐색
    move_list = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    for move in move_list:
        find_warm(x + move[0], y + move[1])


T = int(input())

for tc in range(T):
    M, N, K = map(int, input().split())
    cabbage_list = [[0] * M for _ in range(N)]
    count = 0

    for _ in range(K):
        x, y = map(int, input().split())
        cabbage_list[y][x] = 1

    for i in range(N):
        for j in range(M):
            # 배추 밭에 배추가 있을 때
            if cabbage_list[i][j] == 1:
                find_warm(i, j)
                count += 1

    print(count)
