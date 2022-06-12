import heapq
import sys
sys.stdin = open('M.txt')


def dijkstra():
    while hq:
        cost, cur = heapq.heappop(hq)
        if distance[cur] < cost:
            continue
        for temp_e, temp_c in graph[cur]:
            new_c = temp_c + cost
            if new_c < distance[temp_e]:
                distance[temp_e] = new_c
                heapq.heappush(hq, (new_c, temp_e))

    return distance[D - 1]


# 도시의 개수 N
N = int(sys.stdin.readline())
# 버스의 개수 M
M = int(sys.stdin.readline())
graph = [[] for _ in range(N)]
for _ in range(M):
    s, e, c = map(int, sys.stdin.readline().split())
    graph[s - 1].append([e - 1, c])       # [도착 도시, 비용]
# 출발 도시 S, 도착 도시 D
S, D = map(int, sys.stdin.readline().split())

INF = float('inf')
distance = [INF for _ in range(N)]
distance[S - 1] = 0         # 출발 도시 거리 초기화
hq = []
heapq.heappush(hq, (0, S - 1))      # (비용, 출발 도시)

print(dijkstra())
