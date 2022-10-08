import sys, copy
sys.stdin = open('L.txt')


def dfs(d, r, c, mat, eat, fishes):
    global max_eat
    eat += mat[r][c]                # 현재 위치 물고기 먹기!
    fishes[mat[r][c]][0] = -1       # 먹힌 물고기 => -1
    mat[r][c] = 17                  # 지도에서 상어 위치 => 17

    for i in range(1, 17):
        if fishes[i][0] != -1:
            for j in range(8):      # 막히면 방향 바꿀 수 있도록 하는 for문
                fish = fishes[i]    # [방향, 행, 열]
                f_new_r, f_new_c = fish[1] + moves[(fish[0] + j) % 8][0], fish[2] + moves[(fish[0] + j) % 8][1]
                # 좌표 안벗어나고, 상어가 아니라면!
                if 0 <= f_new_r < 4 and 0 <= f_new_c < 4 and mat[f_new_r][f_new_c] != 17:
                    # 물고기 이동!
                    mat[fish[1]][fish[2]], mat[f_new_r][f_new_c] = mat[f_new_r][f_new_c], mat[fish[1]][fish[2]]
                    if not mat[fish[1]][fish[2]]:   # 만약 빈 자리로 이동이라면, 물고기 dict 정보만 갱신!
                        fishes[i] = [(fish[0] + j) % 8, f_new_r, f_new_c]
                        break
                    temp = [fish[1], fish[2]]       # 그 외, 물고기끼리 dict 정보 갱신!
                    fishes[mat[temp[0]][temp[1]]][1], fishes[mat[temp[0]][temp[1]]][2] = temp[0], temp[1]
                    fishes[i] = [(fish[0] + j) % 8, f_new_r, f_new_c]
                    break
    mat[r][c] = 0                   # 지도에서 상어 위치 => 0, 다음 dfs를 위해 자리 비우기!

    trigger = 0                     # 상어가 먹을 물고기가 있는지 체크할 trigger
    for i in (1, 2, 3):
        new_r, new_c = r + moves[d][0]*i, c + moves[d][1]*i
        if 0 <= new_r < 4 and 0 <= new_c < 4 and mat[new_r][new_c]:
            # 조건에 맞다면, 지도와 물고기dict deepcopy해서 인자로 넘기기!
            dfs(fishes[mat[new_r][new_c]][0], new_r, new_c, copy.deepcopy(mat), eat, copy.deepcopy(fishes))
            trigger = 1

    if not trigger:                 # 먹을거 없으면,
        if eat > max_eat:           # 비교해서 갱신!
            max_eat = eat
        return


mat = [[0]*4 for _ in range(4)]
fishes = {}
moves = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
for i in range(4):
    data = list(map(int, input().split()))
    mat[i] = data[::2]
    for j in range(4):
        a, b = data[2*j], data[2*j+1]
        fishes[a] = [b-1, i, j]
shark = fishes[mat[0][0]]
max_eat = 0
dfs(shark[0], shark[1], shark[2], mat, 0, fishes)
print(max_eat)
