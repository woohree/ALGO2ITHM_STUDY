import sys
import copy
sys.stdin = open('input.txt')

# X, Y축 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# cctv 종류에 따른 감시 방향
direction = [
    [],
    # 1번 카메라
    [[0], [1], [2], [3]],
    # 2번 카메라
    [[0, 2], [1, 3]],
    # 3번 카메라
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    # 4번 카메라
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    # 5번 카메라
    [[0, 1, 2, 3]]]


N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
# cctv 리스트
cctv = []
# cctv 찾기
for i in range(N):
    for j in range(M):
        if room[i][j] != 0 and room[i][j] != 6:
            cctv.append([i, j, room[i][j]])  # x위치, y위치, cctv 종류
# 사각지대 크기(최댓값으로 설정)
ans = 1e9

# 감시 가능 구역을 저장
def watch(x, y, direction, tmp):
    for d in direction:
        nx, ny = x, y
        # 이동할 수 없을 때까지 이동하면서 '#'으로 변경
        while True:
            nx += dx[d]
            ny += dy[d]
            # 이동 가능한 범위를 벗어나거나 벽이면 break
            if nx < 0 or nx >= N or ny < 0 or ny >= M or tmp[nx][ny] == 6:
                break
            # 빈칸이면 감시 구역으로 변경
            elif tmp[nx][ny] == 0:
                tmp[nx][ny] = '#'

# DFS 이용하여 가장 많이 사각지대를 만드는 것을 찾기
def dfs(n, room):
    global ans
    # 맨 처음 방을 깊은 복사
    tmp = copy.deepcopy(room)

    # 만약 끝에 도달했으면 사각지대 최소 크기를 갱신하고 저장
    if n == len(cctv):
        count = 0  # 빈칸 개수
        for t in tmp:
            count += t.count(0)
        ans = min(ans, count)
        return
    # cctv에 있는 값은 x, y축 값과 cctv의 종류
    x, y, c = cctv[n]
    # 해당 cctv의 종류에 따른 감시 구역을 구한다
    for d in direction[c]:
        # 우선 맵을 바꿔봄
        watch(x, y, d, tmp)
        # 그러고나서 최솟값을 저장함
        dfs(n + 1, tmp)
        # 그 후에 다시 리셋해서 반복함
        tmp = copy.deepcopy(room)

dfs(0, room)
print(ans)