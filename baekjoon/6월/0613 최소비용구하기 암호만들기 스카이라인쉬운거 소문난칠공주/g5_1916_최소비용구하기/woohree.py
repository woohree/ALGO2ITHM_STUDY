import sys, heapq
sys.stdin = open('L.txt')


def dijkstra(graph, start):     # 데이크스트라
    inf = float('inf')
    D = [inf] * (N+1)
    D[start] = 0
    news = [(0, start)]

    while news:
        W, now = heapq.heappop(news)
        if W <= D[now]:
            for new_v, w in graph[now]:
                new_w = D[now] + w
                if new_w < D[new_v]:
                    D[new_v] = new_w
                    heapq.heappush(news, (new_w, new_v))

    return D


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, sys.stdin.readline().rstrip().split())
    graph[s].append((e, w))
start, end = map(int, input().split())
ans = dijkstra(graph, start)
print(ans[end])