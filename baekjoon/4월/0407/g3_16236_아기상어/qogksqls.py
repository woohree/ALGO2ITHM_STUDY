# 1시간 지나서야 크기가 큰 물고기 좌표는 못 지나가는거 알았다...
# bfs 사용

import sys, collections
sys.stdin = open('B.txt')


# 92ms
def bfs():
    global dist, answer, eat_fish
    # 먹힐 물고기 담은 리스트
    eaten_fish = []
    # bfs
    while baby_shark:
        for _ in range(len(baby_shark)):
            current = baby_shark.popleft()
            for move in moves:
                if 0 <= current[0] + move[0] < N and 0 <= current[1] + move[1] < N:  # 범위
                    if shark_size >= matrix[current[0] + move[0]][current[1] + move[1]]:  # 이동 가능한 경로
                        if visited[current[0] + move[0]][current[1] + move[1]] == 0:  # 방문하지 않은 곳인 경우
                            baby_shark.append((current[0] + move[0], current[1] + move[1]))
                            visited[current[0] + move[0]][current[1] + move[1]] = 1
                            # eaten_fish 찾는 조건
                            # matrix 의 값이 자연수면서 상어보단 작은 물고기면
                            if shark_size > matrix[current[0] + move[0]][current[1] + move[1]] >= 1:
                                # 비교할 물고기가 채워져 있는 경우
                                if eaten_fish:
                                    # 행 비교
                                    if eaten_fish[0][0] > current[0] + move[0]:
                                        eaten_fish.pop()
                                        eaten_fish.append((current[0] + move[0], current[1] + move[1]))
                                    # 행 같을 경우
                                    elif eaten_fish[0][0] == current[0] + move[0]:
                                        # 열 비교
                                        if eaten_fish[0][1] > current[1] + move[1]:
                                            eaten_fish.pop()
                                            eaten_fish.append((current[0] + move[0], current[1] + move[1]))
                                # 물고기가 아직 안 담긴 경우(초기값 설정)
                                else:
                                    eaten_fish.append((current[0] + move[0], current[1] + move[1]))
        dist += 1
        # 먹힐 물고기 정해진 경우, 할거 하고 return 하면 됨
        if eaten_fish:
            eat_fish += 1
            answer += dist
            baby_shark.clear()
            baby_shark.append((eaten_fish[0][0], eaten_fish[0][1]))
            matrix[eaten_fish[0][0]][eaten_fish[0][1]] = 0
            return


N = int(sys.stdin.readline().rstrip())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# 아기 상어 초기 위치 찾기 & 초기 위치 값 0으로 변환
baby_shark = collections.deque()
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 9:
            baby_shark.append((i, j))
            matrix[i][j] = 0

moves = [[-1, 0], [0, -1], [0, 1], [1, 0]]  # 상, 좌, 우, 하
shark_size, eat_fish = 2, 0
answer = 0
while 1:
    # visited 는 매번 초기화
    visited = [[0] * N for _ in range(N)]
    dist = 0
    # 물고기를 먹었나 안 먹었나를 체크해서 while 문 탈출하는 용도로 씀
    # 물고기 먹은 값이 안 변했을 경우가 엄마한테 가는 경우
    pre_eat_fish = eat_fish
    bfs()
    # 레벨 업
    if eat_fish == shark_size:
        shark_size += 1
        eat_fish = 0
    if pre_eat_fish == eat_fish:
        break

print(answer)

'''
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
# 아기상어 처음 위치, 크기 별 물고기 좌표
baby_shark = []
fishes = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 9:
            baby_shark = [i, j, 2, 0]  # 행, 열, 아기 상어 크기, 먹은 먹이 개수
            matrix[i][j] = 0
        if matrix[i][j] > 0:
            fishes.append([i, j, matrix[i][j]])  # 행, 열, 물고기 크기

time = 0
while 1:
    min_dist = 2 * N
    eaten_fish = []
    for fish in fishes:
        if baby_shark[2] > fish[2]:
            dist = abs(fish[0] - baby_shark[0]) + abs(fish[1] - baby_shark[1])
            if min_dist >= dist:  # 가장 가까운 물고기 찾기
                if min_dist > dist:
                    min_dist = dist
                    eaten_fish = fish
                elif min_dist == dist and eaten_fish[0] >= fish[0]:  # 거리 같은 물고기인 경우, 행 비교
                    if eaten_fish[0] > fish[0]:
                        eaten_fish = fish
                    elif eaten_fish[0] == fish[0] and eaten_fish[1] > fish[1]:  # 거리 같은 물고기인 경우, 열 비교
                        eaten_fish = fish
    if eaten_fish:
        baby_shark[0] = eaten_fish[0]
        baby_shark[1] = eaten_fish[1]
        baby_shark[3] += 1
        if baby_shark[3] == baby_shark[2]:
            baby_shark[2] += 1
            baby_shark[3] = 0
        fishes.remove(eaten_fish)
        time += min_dist
    else:
        break

print(time)
'''