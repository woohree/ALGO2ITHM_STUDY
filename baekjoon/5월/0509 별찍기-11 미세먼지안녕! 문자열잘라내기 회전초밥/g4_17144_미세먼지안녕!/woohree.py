import sys
sys.stdin = open('L.txt')


def misemise(dusts, air_cleaner):
    moves = ((0, 1), (-1, 0), (0, -1), (1, 0))
    air1_r, air1_c = air_cleaner[0]
    air2_r, air2_c = air_cleaner[1]

    for t in range(T):
        temp = {}
        for key, val in dusts.items():                          # 미세먼지 퍼뜨리고 temp에 {좌표: 값}으로 저장
            r, c = key
            temp.setdefault((r, c), 0)
            temp[(r, c)] += val
            for move in moves:
                new_r, new_c = r + move[0], c + move[1]
                if 0 <= new_r < R and 0 <= new_c < C and mat[new_r][new_c] != -1:
                    temp.setdefault((new_r, new_c), 0)
                    temp[(new_r, new_c)] += val // 5
                    temp[(r, c)] -= val // 5

        new_temp = {}
        for key, val in temp.items():                           # 공기청정기 돌리기
            r, c = key
            if (r == 0 or r == R-1) and c != 0:                 # 좌 1
                new_temp[(r, c-1)] = val
            elif (r == air1_r or r == air2_r) and c != C-1:     # 우 1
                new_temp[(r, c+1)] = val
            elif r <= air1_r:
                if c == C-1 and r != 0:                         # 위 1
                    new_temp[(r-1, c)] = val
                elif c == 0:                                    # 아래 1
                    if r+1 != air1_r:
                        new_temp[(r+1, c)] = val
                else:                                           # 영향없는 애들
                    new_temp[(r, c)] = val
            elif r >= air2_r:
                if c == 0:                                      # 위 1
                    if r-1 != air2_r:
                        new_temp[(r-1, c)] = val
                elif c == C-1 and r != R-1:                     # 아래 1
                    new_temp[(r+1, c)] = val
                else:                                           # 영향없는 애들
                    new_temp[(r, c)] = val

        dusts = new_temp

    result = 0
    for val in dusts.values():
        result += val
    return result


R, C, T = map(int, input().split())
mat = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(R)]
air_cleaner = []
dusts = {}
for i in range(R):
    for j in range(C):
        if mat[i][j] > 0:
            dusts[(i, j)] = mat[i][j]
        elif mat[i][j] == -1:
            air_cleaner.append((i, j))

ans = misemise(dusts, air_cleaner)
print(ans)