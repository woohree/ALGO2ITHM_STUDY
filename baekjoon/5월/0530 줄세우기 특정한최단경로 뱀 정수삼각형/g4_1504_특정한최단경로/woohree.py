import sys, heapq
sys.stdin = open('L.txt')


def dijkstra(graph, start):    # 그저 다익스트라
    inf = float('inf')
    D = [inf] * (N+1)
    news = [(0, start)]
    D[start] = 0

    while news:
        W, now = heapq.heappop(news)
        if W <= D[now]:
            for new_v, w in graph[now]:
                new_w = D[now] + w
                if new_w < D[new_v]:
                    D[new_v] = new_w
                    heapq.heappush(news, (new_w, new_v))

    return D


N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    s, e, w = map(int, sys.stdin.readline().rstrip().split())
    graph[s].append((e, w))
    graph[e].append((s, w))
essential_v = list(map(int, sys.stdin.readline().split()))

d1 = dijkstra(graph, 1)                     # 1번 정점부터 모든 정점 최단 거리
d2 = dijkstra(graph, essential_v[0])        # 필수 정점[0]부터 모든 정점 최단 거리
d3 = dijkstra(graph, essential_v[1])        # 필수 정점[1]부터 모든 정점 최단 거리

a = d1[essential_v[0]] + d2[essential_v[1]] + d3[N]  # 1 => 필수1 => 필수2 => N
b = d1[essential_v[1]] + d3[essential_v[0]] + d2[N]  # 1 => 필수2 => 필수1 => N

if a >= float('inf') and b >= float('inf'):  # 경로가 없는 경우(inf값인 경우)
    print(-1)
else:                                        # 경로가 있는 경우
    print(min(a, b))