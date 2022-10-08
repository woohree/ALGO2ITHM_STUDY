import sys, heapq
INF = sys.maxsize
sys.stdin = open('B.txt')

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())


def dijkstra(s, e):
    d = [INF] * (N+1)
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


print(dijkstra(start, end))
