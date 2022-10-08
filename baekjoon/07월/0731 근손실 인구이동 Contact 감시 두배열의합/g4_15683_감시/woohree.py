import sys, copy
sys.stdin = open('W.txt')


def change_mat(mat, r, c, direc):
    for d in direc:
        i = 0
        while 1:
            new_r, new_c = r + moves[d][0] * i, c + moves[d][1] * i
            if 0 <= new_r < N and 0 <= new_c < M and mat[new_r][new_c] != 6:
                if not mat[new_r][new_c]:
                    mat[new_r][new_c] = -1              # 감시할 수 있으면 -1
            else:
                break
            i += 1


def dfs(idx, mat):
    global ans
    if idx == len_cams:                                 # 종료조건, 전체 cctv 다 봤는지 여부
        cnt = 0
        for i in range(N):
            for j in range(M):
                if not mat[i][j]:
                    cnt += 1
        ans = min(ans, cnt)
        return

    r, c, cam = cams[idx]
    copy_mat = copy.deepcopy(mat)
    for direc in cam_direcs[cam]:                       # cctv 번호에 따라서 경우의 수 체크
        change_mat(copy_mat, r, c, direc)               # 감시 가능한 지점 체크
        dfs(idx+1, copy_mat)                            # 다음 cctv
        copy_mat = copy.deepcopy(mat)                   # 돌아오면 지도 복구


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
moves = ((-1, 0), (0, 1), (1, 0), (0, -1))              # 상 우 하 좌
cam_direcs = (                                          # cctv 방향 경우의 수
    0,
    ((0,), (1,), (2,), (3,)),
    ((0, 2), (1, 3)),
    ((0, 1), (1, 2), (2, 3), (3, 0)),
    ((0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)),
    ((0, 1, 2, 3),)
)
cams = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] in (1, 2, 3, 4, 5):
            cams.append((i, j, matrix[i][j]))           # cctv 좌표, cctv 번호
len_cams = len(cams)
ans = 65
dfs(0, matrix)
print(ans)