import sys
import copy
sys.setrecursionlimit(10**6)
sys.stdin = open('G.txt')


def dfs(row, col, value, color):
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for idx in range(4):
        row, col = row+dx[idx], col+dy[idx]
        #적록색약이라면
        if color and 0 <= row < N and 0 <= col < N:
            # R, G는 같은 색깔
            if value in ['R', 'G'] and matrix_color[row][col] in ['R', 'G']:
                matrix_color[row][col] = 'X'
                dfs(row, col, value, 1)
            elif matrix_color[row][col] == value:
                matrix_color[row][col] = 'X'
                dfs(row, col, value, 1)
    
        elif 0 <= row < N and 0 <= col < N and matrix[row][col] == value:
            matrix[row][col] = 'X'
            dfs(row, col, value, 0)
        row, col = row-dx[idx], col-dy[idx]


N = int(input())

matrix = [list(input()) for _ in range(N)]
matrix_color = copy.deepcopy(matrix)
cnt, cnt_color = 0, 0
for row in range(N):
    for col in range(N):
        if matrix[row][col] != 'X':
            value = matrix[row][col]
            matrix[row][col] = 'X'
            cnt += 1
            dfs(row, col, value, 0)
        if matrix_color[row][col] != 'X':
            value_color = matrix_color[row][col]
            matrix_color[row][col] = 'X'
            cnt_color += 1
            dfs(row, col, value_color, 1)
 
print(cnt, cnt_color)