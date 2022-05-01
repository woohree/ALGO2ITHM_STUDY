import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('L.txt')


def dfs_outer(r, c):        # 상온 지역 2로 만들기
    mat[r][c] = 2
    for move in moves:
        new_r, new_c = r + move[0], c + move[1]
        if 0 <= new_r < N and 0 <= new_c < M and not mat[new_r][new_c] and not visited_outer[new_r][new_c]:
            visited_outer[new_r][new_c] = 1
            dfs_outer(new_r, new_c)


def melt_cheese(r, c):      # 치즈 녹이기 + 살아있는 치즈 체크
    cnt = 0
    for move in moves:
        new_r, new_c = r + move[0], c + move[1]
        if 0 <= new_r < N and 0 <= new_c < M and mat[new_r][new_c] == 2:
            cnt += 1
        if cnt >= 2:
            mat[r][c] = 0
            blanks.append((r, c))
            return
    new_cheeses.append((r, c))


N, M = map(int, sys.stdin.readline().split())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
cheeses = []
for i in range(N):                  # 치즈 좌표 구하기
    for j in range(M):
        if mat[i][j]:
            cheeses.append((i, j))

visited_outer = [[0]*M for _ in range(N)]
for i, j in ((0, 0), (N-1, M-1), (0, M-1), (N-1, 0)):
    if not visited_outer[i][j]:     # 가장자리에서 상온 지역 만들기
        visited_outer[i][j] = 1
        dfs_outer(i, j)

time = 0
while 1:
    if not cheeses:                 # 더이상 치즈가 없으면 끝!
        break
    blanks = []                     # 녹은 치즈 좌표(상온 지역)
    new_cheeses = []                # 살아있는 치즈 좌표
    for r, c in cheeses:            # 치즈 녹이기
        melt_cheese(r, c)
    cheeses = new_cheeses
    time += 1
    for r, c in blanks:             # 상온 지역 갱신
        if not visited_outer[r][c]:
            visited_outer[r][c] = 1
            dfs_outer(r, c)

print(time)