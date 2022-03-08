import sys
sys.stdin = open('L.txt')
sys.setrecursionlimit(10**7)


def change_visited_True(row, col):
    visited[row][col] = True  # 방문도장 쾅!!
    moves = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, 1], [1, 1], [1, -1], [-1, -1]]  # 가로세로대각선 체크
    for move in moves:
        new_row, new_col = row+move[0], col+move[1]
        if 0 <= new_row < h and 0 <= new_col < w:
            if not visited[new_row][new_col]:
                if matrix[new_row][new_col] == 1:  # 1인 지점만 찾아 방문도장찍을 수 있도록 설정
                    change_visited_True(new_row, new_col)


while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    matrix = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0  # 섬의 갯수 카운트
    visited = [[False]*w for _ in range(h)]
    # 지도돌면서 방문안한 1 지점에서 재귀 시작
    for row in range(h):
        for col in range(w):
            if not visited[row][col] and matrix[row][col] == 1:
                cnt += 1
                change_visited_True(row, col)
    print(cnt)