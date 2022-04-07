from collections import deque
import heapq
import sys
sys.stdin = open('G.txt')

def bfs(x, y):
    global baby_shark, eat_fish, time

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while True:
        # 아기 상어 좌표, 이동 거리
        queue = deque()
        queue.append((x, y, 0))

        # 먹을 수 있는 물고기
        heap = []
        # 최소 이동 시간 
        min_move = N ** 2

        # 방문 배열 초기화
        visited = [[0 for _ in range(N)] for _ in range(N)]
        visited[x][y] = 1

        while queue:
            position_x, position_y, dist = queue.popleft()

            # 거리가 최소 이동 거리보다 크면 중단
            if dist > min_move:
                break
            
            for idx in range(4):
                new_x, new_y = position_x + dx[idx], position_y + dy[idx]
                # 인덱스 범위를 벗어나지 않고, 아기 상어보다 물고기의 크기가 작거나 같을때
                if 0 <= new_x < N and 0 <= new_y < N and not visited[new_x][new_y] and matrix[new_x][new_y] <= baby_shark:
                    # 해당 범위 안에서만 물고기 먹기
                    if 0 < matrix[new_x][new_y] < baby_shark:
                        # 먹을 수 있는 물고기로 추가
                        heapq.heappush(heap, (new_x, new_y, dist + 1))
                        min_move = dist
                    
                    queue.append((new_x, new_y, dist + 1))
                    visited[new_x][new_y] = 1
        # 먹을 수 있는 물고기가 있다면
        if len(heap):
            # 함수 인자 값을 x, y로 설정해줘서 물고기 좌표도 x, y로 설정..........
            x, y, move = heapq.heappop(heap)
            time += move
            eat_fish += 1
            matrix[x][y] = 0

            if eat_fish == baby_shark:
                baby_shark += 1
                eat_fish = 0
        else:
            break



N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 아기 상어 크기, 먹은 물고기 수, 이동 시간
baby_shark, eat_fish, time = 2, 0, 0

for row in range(N):
    for col in range(N):
        if matrix[row][col] == 9:
            shark = (row, col)
            matrix[row][col] = 0
            break
bfs(shark[0], shark[1])
print(time)