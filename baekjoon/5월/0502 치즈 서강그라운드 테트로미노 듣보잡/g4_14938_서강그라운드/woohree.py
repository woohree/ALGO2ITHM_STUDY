import sys, heapq
sys.stdin = open('L.txt')


def dijkstra(start):
    inf = float('inf')
    D = [inf] * (n+1)
    news = [(0, start)]
    D[start] = 0

    while news:
        now_w, now = heapq.heappop(news)
        if now_w <= D[now]:
            for new, w in graph[now]:
                new_w = D[now] + w
                if new_w < D[new]:
                    D[new] = new_w
                    heapq.heappush(news, (new_w, new))
    return D


n, m, r = map(int, sys.stdin.readline().split())
item_points = [0] + list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n+1)]
for _ in range(r):
    s, e, w = map(int, sys.stdin.readline().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

ans = 0
for i in range(1, n+1):
    D = dijkstra(i)                         # 모든 점에서 다익스트라 돌리기
    now_items = 0
    for j in range(1, n+1):                 # 각 지점까지 최소 비용이 m과 같거나, 크면,
        if D[j] <= m:
            now_items += item_points[j]     # 아이템 챙기기
    ans = max(ans, now_items)

print(ans)