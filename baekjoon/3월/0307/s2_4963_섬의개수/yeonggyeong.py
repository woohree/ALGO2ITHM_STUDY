import sys
sys.stdin = open('G.txt')
sys.setrecursionlimit(10**6)


def dfs(x, y):
# 상 우 하 좌 대각선
    dx = [-1, 0, 1, 0, -1, -1, 1, 1]
    dy = [0, 1, 0, -1, -1, 1, 1, -1]

    # 8방향으로 이동 후 땅이면 dfs 반복
    # 방문한 땅은 0으로 변경
    for i in range(8):
        new_x, new_y = x+dx[i], y+dy[i]
        if 0 <= new_x < h and 0 <= new_y < w and matrix[new_x][new_y] == 1:
            matrix[new_x][new_y] = 0
            dfs(new_x, new_y)

while True:
    w, h = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(h)]
    # 마지막 행 조건 들어오면 break
    if [w, h] == [0 ,0]:
        break

    # 섬의 개수 카운트
    island = 0
    for row in range(h):
        for col in range(w):
            # 해당 위치가 땅이면 dfs 실행
            if matrix[row][col] == 1:
                island += 1
                matrix[row][col] = 0
                dfs(row, col)

    print(island)