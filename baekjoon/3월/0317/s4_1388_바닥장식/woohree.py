import sys
sys.stdin = open('L.txt')


def how_many_woods_i_need(floors):
    for row in range(N):
        for col in range(M):
            if floors[row][col] == '-':                 # '-'에서 dfs_row 시작!
                if not visited_row[row][col]:
                    dfs_row(row, col)
            elif floors[row][col] == '|':               # '|'에서 dfs_col 시작!
                if not visited_col[row][col]:
                    dfs_col(row, col)


def dfs_row(r, c):
    global cnt_row
    visited_row[r][c] = True
    if c == M-1 or floors[r][c+1] == '|':               # 가로로 이어진 '-'가 끝나면,
        cnt_row += 1                                    # cnt_row += 1
    elif not visited_row[r][c+1]:
        if floors[r][c+1] == '-':
            dfs_row(r, c+1)


def dfs_col(r, c):
    global cnt_col
    visited_col[r][c] = True
    if r == N-1 or floors[r+1][c] == '-':               # 세로로 이어진 '|'가 끝나면,
        cnt_col += 1                                    # cnt_col += 1
    elif not visited_col[r+1][c]:
        if floors[r+1][c] == '|':
            dfs_col(r+1, c)


N, M = map(int, sys.stdin.readline().rstrip().split())
floors = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]
visited_row = [[False]*M for _ in range(N)]
visited_col = [[False]*M for _ in range(N)]
cnt_row = cnt_col = 0
how_many_woods_i_need(floors)
print(cnt_row+cnt_col)
