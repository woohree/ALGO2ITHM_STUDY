from itertools import combinations
from collections import deque
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

sys.stdin = open('input.txt')

# 값 입력
# N은 배열 크기, M은 바이러스 선택 갯수
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 정답(최솟값 구하는 거니까 최댓값으로 설정)
result = 2501

# 바이러스 놓을 경우의 수 구하기
virus = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            # x축 y축 값과 count(거리)를 값으로 추가함
            virus.append([i, j, 0])
virus_combi = list(combinations(virus, M))

# BFS 이용
for i in range(len(virus_combi)):
    k = 0
    queue = deque(virus_combi[i])
    visited = [[False]*N for _ in range(N)]
    while queue:
        a, b, count = queue.popleft()
        visited[a][b] = True
        for j in range(4):
            na = a+dx[j]
            nb = b+dy[j]
            if 0<= na < N and 0<= nb < N:
                if graph[na][nb] == 0 and visited[na][nb] == False:
                    visited[na][nb] = True
                    queue.append([na, nb, count+1])
                    k = max(k, count+1)
                # 바이러스 만나면 그냥 이동 처리만
                elif graph[na][nb] == 2 and visited[na][nb] == False:
                    queue.append([na, nb, count+1])
    for j in range(N):
        for l in range(N):
            if not visited[j][l] and not graph[j][l]:
                k = 2501
    result = min(result, k)
if result == 2501:
    print(-1)
else:
    print(result)