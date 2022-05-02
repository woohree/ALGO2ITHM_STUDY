import sys
sys.stdin = open('M.txt')


def floyd_warshall():
    for k in range(N):          # 경유지
        dist[k][k] = 0
        for s in range(N):      # 출발지
            for e in range(N):  # 도착지
                dist[s][e] = min(dist[s][k] + dist[k][e], dist[s][e])


# 지역의 개수 N, 수색 범위 M, 길의 개수 R
N, M, R = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))

INF = float('inf')
dist = [[INF] * N for _ in range(N)]    # 모든 거리를 최대로 초기화
for _ in range(R):
    u, v, w = map(int, sys.stdin.readline().split())
    dist[u - 1][v - 1] = min(dist[u - 1][v - 1], w)
    dist[v - 1][u - 1] = min(dist[v - 1][u - 1], w)

floyd_warshall()

max_item = 0
for i in range(N):
    temp_item = 0
    for j in range(N):
        if dist[i][j] <= M:
            temp_item += items[j]
    max_item = max(max_item, temp_item)
print(max_item)
