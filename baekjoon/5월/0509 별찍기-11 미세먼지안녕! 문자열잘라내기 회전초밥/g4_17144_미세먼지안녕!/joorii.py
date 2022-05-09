# python3 시간초과, pypy3 통과
import math
import sys
sys.stdin = open('M.txt')


def spread_dust():
    new_matrix = [[0 for _ in range(C)] for _ in range(R)]
    for ar in air_purifier:             # 공기청정기 좌표 표시
        new_matrix[ar][0] = -1

    moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for dust in dusts:
        cur_r, cur_c = dust
        next_dust = math.floor(matrix[cur_r][cur_c] / 5)
        cnt = 0
        for move in moves:      # 미세먼지 확산
            next_r, next_c = cur_r + move[0], cur_c + move[1]
            if 0 <= next_r < R and 0 <= next_c < C and matrix[next_r][next_c] != -1:
                new_matrix[next_r][next_c] += next_dust
                cnt += 1
        new_matrix[cur_r][cur_c] += matrix[cur_r][cur_c] - next_dust * cnt

    return new_matrix


def purify():
    cw = ((0, 1), (1, 0), (0, -1), (-1, 0))     # 시계방향
    ccw = ((0, 1), (-1, 0), (0, -1), (1, 0))    # 반시계방향

    temp, cnt = 0, 0     # 방향 전환 횟수
    cur_r, cur_c = air_purifier[0], 0       # 위쪽 방향 부터(시계 반대 방향)
    while 1:
        next_r, next_c = cur_r + ccw[cnt][0], cur_c + ccw[cnt][1]
        if 0 <= next_r <= air_purifier[0] and 0 <= next_c < C:
            if matrix[next_r][next_c] == -1:    # 공기 청정기에 돌아왔을 떄
                break
            temp, matrix[next_r][next_c] = matrix[next_r][next_c], temp
            cur_r, cur_c = next_r, next_c
        else:
            cnt += 1

    temp, cnt = 0, 0
    cur_r, cur_c = air_purifier[1], 0       # 아래 방향 (시계 방향)
    while 1:
        next_r, next_c = cur_r + cw[cnt][0], cur_c + cw[cnt][1]
        if air_purifier[1] <= next_r < R and 0 <= next_c < C:
            if matrix[next_r][next_c] == -1:
                break
            temp, matrix[next_r][next_c] = matrix[next_r][next_c], temp
            cur_r, cur_c = next_r, next_c
        else:
            cnt += 1


# 세로 길이 R, 가로 길이 C, 초 T
R, C, T = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

for _ in range(T):
    air_purifier = []                   # 공기청정기 좌표
    dusts = []                          # 미세먼지 좌표
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == -1:      # 공기청정기
                air_purifier.append(i)
            elif matrix[i][j]:
                dusts.append((i, j))

    matrix = spread_dust()
    purify()

ans = 0
for i in range(R):
    ans += sum(matrix[i])
print(ans + 2)
