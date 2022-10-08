import heapq
import sys
sys.stdin = open('M.txt')


def dijkstra(s):
    distance = [INF for _ in range(N)]
    distance[s] = 0     # 시작 정점 초기화
    hq = []
    heapq.heappush(hq, (0, s))  # (거리, 시작정점)

    while hq:
        cost, cur = heapq.heappop(hq)
        if distance[cur] < cost:
            continue
        for temp_u, temp_c in graph[cur]:
            new_c = temp_c + cost
            if new_c < distance[temp_u]:
                distance[temp_u] = new_c
                heapq.heappush(hq, (new_c, temp_u))

    return distance


INF = float('inf')
# 정점의 개수 N, 간선의 개수 E
N, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a - 1].append([b - 1, c])     # [도착정점, 거리]
    graph[b - 1].append([a - 1, c])

v1, v2 = map(int, sys.stdin.readline().split())

start = dijkstra(0)         # 1번 정점이 시작점
mid = dijkstra(v1 - 1)      # 중간 정점 v1이 시작점
end = dijkstra(N - 1)       # N번 정점이 시작점

answer = min(start[v1 - 1] + mid[v2 - 1] + end[v2 - 1], start[v2 - 1] + mid[v2 - 1] + end[v1 - 1])
print(-1) if answer < 0 or answer == INF else print(answer)
