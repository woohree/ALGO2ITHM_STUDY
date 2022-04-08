from collections import deque
import heapq
import sys
sys.stdin = open('M.txt')


def baby_shark():
    global shark

    # 상 좌 우 하 -> 방향 우선순위로는 불가능...
    d = ((-1, 0), (0, -1), (0, 1), (1, 0))
    time = 0
    # 상어의 크기
    shark_weight = temp = 2
    # [상어와의 거리, 행 인덱스, 열 인덱스]
    nexts = deque([shark])
    fishes = []
    visited = [[False] * N for _ in range(N)]
    visited[shark[1]][shark[2]] = True

    while nexts:
        # bfs로 가장 가까운 거리의 먹을 수 있는 물고기 찾기
        for _ in range(len(nexts)):
            cur = nexts.popleft()

            for i in range(4):
                next_r, next_c = cur[1] + d[i][0], cur[2] + d[i][1]
                # 범위를 벗어나지 않을 때
                if 0 <= next_r < N and 0 <= next_c < N and not visited[next_r][next_c]:
                    # 가장 가까운 거리의 먹을 수 있는 물고기를 찾았을 때
                    if 0 < matrix[next_r][next_c] < shark_weight:
                        fishes.append([cur[0] + 1, next_r, next_c])
                        visited[next_r][next_c] = True
                    # 크기가 큰 물고기가 있어 지나갈 수 없을 때
                    elif matrix[next_r][next_c] > shark_weight:
                        visited[next_r][next_c] = True
                    else:
                        nexts.append([cur[0] + 1, next_r, next_c])
                        visited[next_r][next_c] = True
        # (동일한 거리에 위치한) 물고기를 찾았다면
        if fishes:
            hq = []
            for fish in fishes:
                # [거리, 행 인덱스, 열 인덱스] 정렬
                heapq.heappush(hq, [fish[0], fish[1], fish[2]])

            target = heapq.heappop(hq)
            fishes = []
            temp -= 1
            if temp == 0:                               # 상어 크기 만큼의 물고기를 먹었을 때
                shark_weight += 1                       # 상어 크기 1 증가
                temp = shark_weight
            matrix[target[1]][target[2]] = 0
            time += target[0]                           # 물고기와의 거리만큼 시간 증가
            shark = [0, target[1], target[2]]           # 상어 위치 변경
            nexts = deque([shark])
            visited = [[False] * N for _ in range(N)]
            visited[target[1]][target[2]] = True

    print(time)


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

shark = []
# 아기 상어 위치 찾기
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 9:
            shark = [0, i, j]
            matrix[i][j] = 0

baby_shark()
