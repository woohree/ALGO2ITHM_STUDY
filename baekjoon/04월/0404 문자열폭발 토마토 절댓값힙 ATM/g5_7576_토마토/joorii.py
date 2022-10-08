from collections import deque
import sys
sys.stdin = open('M.txt')


def ripen_tomato():
    # 상 하 좌 우
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))

    nexts = deque()
    # 익은 토마토의 위치를 nexts에 초기화
    for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == 1:
                nexts.append([i, j])

    # bfs
    while nexts:
        cur = nexts.popleft()
        for i in range(4):
            if 0 <= cur[0] + d[i][0] < N and 0 <= cur[1] + d[i][1] < M and tomatoes[cur[0] + d[i][0]][cur[1] + d[i][1]] == 0:
                nexts.append([cur[0] + d[i][0], cur[1] + d[i][1]])
                tomatoes[cur[0] + d[i][0]][cur[1] + d[i][1]] = tomatoes[cur[0]][cur[1]] + 1

    # 탐색 후 방문 못한 곳이 있는지, 혹은 모두 익은 일수 찾기
    ans = 0
    for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == 0:         # 방문 못한 곳이 있을 때, 즉 안 익은 토마토를 발견하면
                return -1
            elif tomatoes[i][j] > ans:      # 토마토가 익은 일수가 가장 큰 숫자 찾기
                ans = tomatoes[i][j]

    return ans - 1


M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]
print(ripen_tomato())
