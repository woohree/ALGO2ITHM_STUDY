import sys
sys.stdin = open('M.txt')


def floyd_warshall():
    for k in range(N):          # 경유지
        costs[k][k] = 0
        for s in range(N):      # 출발지
            for e in range(N):  # 도착지
                costs[s][e] = min(costs[s][e], costs[s][k] + costs[k][e])


# 도시의 개수 N
N = int(sys.stdin.readline())
# 버스의 개수 M
M = int(sys.stdin.readline())

INF = float('inf')
costs = [[INF] * N for _ in range(N)]           # 모든 거리를 최대로 초기화
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    costs[a - 1][b - 1] = min(costs[a - 1][b - 1], c)

floyd_warshall()

for i in range(N):
    for j in range(N):
        print(costs[i][j], end=' ') if costs[i][j] != INF else print(0, end=' ')
    print()
