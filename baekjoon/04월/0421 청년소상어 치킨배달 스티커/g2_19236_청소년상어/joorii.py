import copy
import sys
from collections import deque

sys.stdin = open('M.txt')


def teen_shark():
    moves = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))

    n = matrix[0][0]
    f = fish_dic[n]
    matrix[0][0] = -1  # 상어 위치 -1
    fish_dic[n] = None  # 잡아 먹힌 물고기 None
    # [행 인덱스, 열 인덱스, 이동 방향, 물고기 총합, mat, dic]
    s = [f[0], f[1], f[2], n, copy.deepcopy(matrix), copy.deepcopy(fish_dic)]

    nexts = deque()
    nexts.append(s)
    max_total = 0

    while nexts:
        shark = nexts.popleft()
        mat = shark[4]
        dic = shark[5]

        for i in range(1, 17):      # 물고기 이동
            if dic[i]:          # 물고기가 잡아먹히지 않았을 때
                fish_r, fish_c, fish_d = dic[i][0], dic[i][1], dic[i][2]
                for c in range(1, 8):
                    next_r, next_c = fish_r + moves[fish_d][0], fish_c + moves[fish_d][1]
                    if 0 <= next_r < 4 and 0 <= next_c < 4 and mat[next_r][next_c] != -1:   # 다음 좌표가 범위 안이고 상어가 없을 때
                        target = mat[next_r][next_c]
                        mat[fish_r][fish_c], mat[next_r][next_c] = mat[next_r][next_c], mat[fish_r][fish_c]
                        dic[i] = [next_r, next_c, fish_d]
                        if target is not None:     # 다른 물고기가 있을 때
                            dic[target][0], dic[target][1] = fish_r, fish_c
                        break
                    else:
                        fish_d = (fish_d + 1) % 8

        for i in range(1, 4):       # 상어 이동
            nr, nc = shark[0] + (moves[shark[2]][0] * i), shark[1] + (moves[shark[2]][1] * i)
            if 0 <= nr < 4 and 0 <= nc < 4 and mat[nr][nc]:     # 다음 좌표가 범위 안이고 물고기가 있을 때
                target = mat[nr][nc]
                target_f = dic[target]
                m, d = copy.deepcopy(mat), copy.deepcopy(dic)
                m[shark[0]][shark[1]], m[nr][nc] = None, -1        # 원래 상어 위치 None, 다음 상어 위치 -1
                d[target] = None
                # [행 인덱스, 열 인덱스, 이동 방향, 물고기 총합, mat, dic]
                nexts.append([nr, nc, target_f[2], shark[3] + target, m, d])

        if max_total < shark[3]:
            max_total = shark[3]

    return max_total


inputs = [list(map(int, input().split())) for _ in range(4)]
matrix = [[] for _ in range(4)]
fish_dic = {}       # key = [행 인덱스, 열 인덱스, 이동 방향]

for i in range(4):
    for j in range(4):
        matrix[i].append(inputs[i][j * 2])
        fish_dic.setdefault(inputs[i][j * 2], [i, j, inputs[i][j * 2 + 1] - 1])

print(teen_shark())
