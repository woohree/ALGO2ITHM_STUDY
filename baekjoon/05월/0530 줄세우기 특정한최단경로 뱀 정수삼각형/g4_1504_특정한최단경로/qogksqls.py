import sys, heapq
sys.stdin = open('B.txt')

INF = float(1e9)
N, E = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, sys.stdin.readline().rstrip().split())


def dijkstra(s, e):
    d = [INF] * (N + 1)
    d[s] = 0
    q = [[0, s]]
    while q:
        dist, now = heapq.heappop(q)
        if dist > d[now]:
            continue
        for v, w in graph[now]:
            if d[v] > d[now] + w:
                d[v] = d[now] + w
                heapq.heappush(q, [d[v], v])
    return d[e]


answer = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N), dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N))
if answer >= INF:
    print(-1)
else:
    print(answer)
