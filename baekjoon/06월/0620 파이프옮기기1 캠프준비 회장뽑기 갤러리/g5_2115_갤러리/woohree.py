import sys
sys.stdin = open('L.txt')


def make_gallery(mat):
    visited_row_above = [[0] * M for _ in range(N)]
    visited_row_below = [[0] * M for _ in range(N)]
    row_cnt = 0
    for i in range(N):                                  # 가로 검사
        for j in range(M-1):
            if mat[i][j] == '.' and mat[i][j+1] == '.':
                if i == 0:                              # 맨 윗줄 => 아랫 벽만 검사
                    if not visited_row_below[i+1][j] and not visited_row_below[i+1][j+1] and mat[i+1][j] == 'X' and mat[i+1][j+1] == 'X':
                        visited_row_below[i+1][j], visited_row_below[i+1][j+1] = 1, 1
                        row_cnt += 1
                elif i == N-1:                          # 맨 밑줄 => 윗 벽만 검사
                    if not visited_row_above[i-1][j] and not visited_row_above[i-1][j+1] and mat[i-1][j] == 'X' and mat[i-1][j+1] == 'X':
                        visited_row_above[i-1][j], visited_row_above[i-1][j+1] = 1, 1
                        row_cnt += 1
                else:                                   # 그 외, 위, 아래 벽 검사
                    if not visited_row_above[i-1][j] and not visited_row_above[i-1][j+1] and mat[i-1][j] == 'X' and mat[i-1][j+1] == 'X':
                        visited_row_above[i-1][j], visited_row_above[i-1][j+1] = 1, 1
                        row_cnt += 1
                    if not visited_row_below[i+1][j] and not visited_row_below[i+1][j+1] and mat[i+1][j] == 'X' and mat[i+1][j+1] == 'X':
                        visited_row_below[i+1][j], visited_row_below[i+1][j+1] = 1, 1
                        row_cnt += 1

    visited_col_left = [[0] * M for _ in range(N)]
    visited_col_right = [[0] * M for _ in range(N)]
    col_cnt = 0
    for j in range(M):                                  # 세로 검사
        for i in range(N-1):
            if mat[i][j] == '.' and mat[i+1][j] == '.':
                if j == 0:                              # 맨 왼쪽 줄 => 오른쪽 벽만 검사
                    if not visited_col_right[i][j+1] and not visited_col_right[i+1][j+1] and mat[i][j+1] == 'X' and mat[i+1][j+1] == 'X':
                        visited_col_right[i][j+1], visited_col_right[i+1][j+1] = 1, 1
                        col_cnt += 1
                elif j == M-1:                          # 맨 오른쪽 줄 => 왼쪽 벽만 검사
                    if not visited_col_left[i][j-1] and not visited_col_left[i+1][j-1] and mat[i][j-1] == 'X' and mat[i+1][j-1] == 'X':
                        visited_col_left[i][j-1], visited_col_left[i+1][j-1] = 1, 1
                        col_cnt += 1
                else:                                   # 그 외, 오른쪽, 왼쪽 벽 검사
                    if not visited_col_left[i][j-1] and not visited_col_left[i+1][j-1] and mat[i][j-1] == 'X' and mat[i+1][j-1] == 'X':
                        visited_col_left[i][j-1], visited_col_left[i+1][j-1] = 1, 1
                        col_cnt += 1
                    if not visited_col_right[i][j+1] and not visited_col_right[i+1][j+1] and mat[i][j+1] == 'X' and mat[i+1][j+1] == 'X':
                        visited_col_right[i][j+1], visited_col_right[i+1][j+1] = 1, 1
                        col_cnt += 1

    return row_cnt + col_cnt


N, M = map(int, input().split())
mat = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
ans = make_gallery(mat)
# print(mat)
print(ans)