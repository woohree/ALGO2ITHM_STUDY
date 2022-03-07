import sys
sys.stdin = open('M.txt')
# 백준 재귀 최대 깊이 제한 1000
sys.setrecursionlimit(10**6)


def get_island_count(i, j):
    # 가로, 세로, 대각선
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]

    # 섬인데 방문한 적 없을 때
    if island_map[i][j] == 1 and visited[i][j] == 0:
        visited[i][j] = 1
        # 가로, 세로, 대각선 탐색
        for k in range(len(dx)):
            # 탐색할 곳이 범위 안에 위치할 떄
            if 0 <= i + dy[k] < h and 0 <= j + dx[k] < w:
                # 이어진 섬이 존재할 때
                if island_map[i + dy[k]][j + dx[k]] == 1 and visited[i + dy[k]][j + dx[k]] == 0:
                    get_island_count(i + dy[k], j + dx[k])

        # 하나로 이어진 섬들을 모두 탐색한 후 1 반환
        return 1

    else:
        return 0


while 1:
    w, h = map(int, input().split())

    # 종료조건 0 0
    if not w and not h:
        break

    island_map = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    count = 0

    # 모든 칸을 돌면서 섬의 개수 탐색
    for i in range(h):
        for j in range(w):
            count += get_island_count(i, j)

    print(count)


