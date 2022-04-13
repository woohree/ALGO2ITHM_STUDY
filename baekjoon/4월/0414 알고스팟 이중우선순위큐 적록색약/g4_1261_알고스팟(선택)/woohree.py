import sys, heapq
sys.stdin = open('L.txt')


def dijkstra():                             # 벽이 있으면 가중치+1 하는 다익스트라
    moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
    inf = N*M
    D = [[inf]*N for _ in range(M)]
    D[0][0] = 0
    news = [(0, (0, 0))]                    # 가중치, 시작점

    while news:
        w, now = heapq.heappop(news)
        if w <= D[now[0]][now[1]]:
            for move in moves:
                new_r, new_c = now[0] + move[0], now[1] + move[1]
                new_w = D[now[0]][now[1]]   # 일단 새 가중치는 해당 지점까지의 최소값
                if 0 <= new_r < M and 0 <= new_c < N:
                    if mat[new_r][new_c]:   # 벽이면 가중치+1
                        new_w += 1
                    if new_w < D[new_r][new_c]:
                        D[new_r][new_c] = new_w
                        heapq.heappush(news, (new_w, (new_r, new_c)))
    return D


N, M = map(int, sys.stdin.readline().split())
mat = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(M)]
ans = dijkstra()
print(ans[M-1][N-1])                        # 최우측 최하단 지점까지 가는 최소 비용
