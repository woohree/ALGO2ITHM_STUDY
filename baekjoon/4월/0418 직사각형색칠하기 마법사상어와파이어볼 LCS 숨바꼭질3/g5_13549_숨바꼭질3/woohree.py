import sys, heapq
sys.stdin = open('L.txt')


def dijkstra(N, K):
    inf = float('inf')
    if N >= K:                              # 시작점이 더 크면 그 이상 갈 필요x
        x = N
    else:                                   # 도착점이 더 크면 그곳보다 +1만큼만 더 갈 수 있음
        x = K+1
    D = [inf] * (x+1)
    news = [(0, N)]
    D[N] = 0

    while news:                             # 다익스트라~~~
        w, now = heapq.heappop(news)
        if w <= D[now]:
            moves = (now-1, now+1, now*2)
            for i in range(3):
                if 0 <= moves[i] <= x:
                    new_w, new = D[now] + 1, moves[i]
                    if i == 2:
                        new_w -= 1
                    if new_w < D[new]:
                        D[new] = new_w
                        heapq.heappush(news, (new_w, new))
    return D[K]


N, K = map(int, input().split())
ans = dijkstra(N, K)
print(ans)
