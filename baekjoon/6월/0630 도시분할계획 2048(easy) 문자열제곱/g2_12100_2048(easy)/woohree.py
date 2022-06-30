import sys, copy
sys.stdin = open('L.txt')


def game_2048(mat, cnt):
    global ans
    if cnt == 5:                                # 종료조건
        ans = max(ans, max(sum(mat, [])))       # 질문탭에서 본 코드 ㅋ.ㅋ
        return

    for m in range(4):                          # 매번 지도 복사하면서 dfs
        game_2048(move_2048(copy.deepcopy(mat), m), cnt+1)


def move_2048(mat, m):
    if m == 0:                                  # 하
        for j in range(N):
            last = N-1                          # 마지막 지점(맨 아래)
            for i in range(N-2, -1, -1):        # 마지막 전 지점부터 탐색
                if mat[i][j]:                   # 0이 아닌 경우,
                    n = mat[i][j]               # 변수에 저장하고 해당 지점 0으로 바꿈
                    mat[i][j] = 0
                    if not mat[last][j]:        # 마지막 지점이 0인 경우,
                        mat[last][j] = n        # n으로 바꾸기(이동)
                        continue                # last 갱신x
                    elif mat[last][j] == n:     # n과 같은 경우,
                        mat[last][j] = 2*n      # 두배해서 저장
                    else:                       # 그 외,
                        mat[last-1][j] = n      # 마지막 전 지점으로 이동
                    last -= 1                   # 마지막 지점 갱신

    elif m == 1:                                # 상
        for j in range(N):                      # 이하동문!
            last = 0
            for i in range(1, N):
                if mat[i][j]:
                    n = mat[i][j]
                    mat[i][j] = 0
                    if not mat[last][j]:
                        mat[last][j] = n
                        continue
                    elif mat[last][j] == n:
                        mat[last][j] = 2*n
                    else:
                        mat[last+1][j] = n
                    last += 1

    elif m == 2:                                # 우
        for i in range(N):
            last = N-1
            for j in range(N-2, -1, -1):
                if mat[i][j]:
                    n = mat[i][j]
                    mat[i][j] = 0
                    if not mat[i][last]:
                        mat[i][last] = n
                        continue
                    elif mat[i][last] == n:
                        mat[i][last] = 2*n
                    else:
                        mat[i][last-1] = n
                    last -= 1

    else:                                       # 좌
        for i in range(N):
            last = 0
            for j in range(1, N):
                if mat[i][j]:
                    n = mat[i][j]
                    mat[i][j] = 0
                    if not mat[i][last]:
                        mat[i][last] = n
                        continue
                    elif mat[i][last] == n:
                        mat[i][last] = 2*n
                    else:
                        mat[i][last+1] = n
                    last += 1
    return mat


N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
ans = 0
game_2048(mat, 0)
print(ans)