import sys, heapq
sys.stdin = open('L.txt')


def dijkstra(graph, start, end):    # 그저 다익스트라
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

    return D[end]


N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    s, e, w = map(int, sys.stdin.readline().rstrip().split())
    graph[s].append((e, w))
    graph[e].append((s, w))
essential_v = list(map(int, sys.stdin.readline().split()))

# 필수 방문 정점까지 다익스트라 각각 돌리기
a = dijkstra(graph, 1, essential_v[0]) + dijkstra(graph, essential_v[0], essential_v[1]) + dijkstra(graph, essential_v[1], N)
b = dijkstra(graph, 1, essential_v[1]) + dijkstra(graph, essential_v[1], essential_v[0]) + dijkstra(graph, essential_v[0], N)
if a >= float('inf') and b >= float('inf'):  # 경로가 없는 경우(inf값인 경우)
    print(-1)
else:                                        # 경로가 있는 경우
    print(min(a, b))