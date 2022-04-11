import sys, heapq
sys.stdin = open('L.txt')


def dijkstra(start, graph):
    min_T = [inf] * (N+1)
    news = [(0, start)]
    min_T[start] = 0

    while news:                                 # 다익스트라
        T, now = heapq.heappop(news)
        if T <= min_T[now]:
            for new_village, t in graph[now]:
                new_T = min_T[now] + t
                if new_T < min_T[new_village]:
                    min_T[new_village] = new_T
                    heapq.heappush(news, (new_T, new_village))

    return min_T                                # 최소 시간 리스트 반환


N, M, X = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N+1)]                # 시작점 -> 도착점 비용
graph_reverse = [[] for _ in range(N+1)]        # 도착점 <- 시작점 비용
inf = float('inf')
for _ in range(M):
    s, e, t = map(int, sys.stdin.readline().rstrip().split())
    graph[s].append((e, t))
    graph_reverse[e].append((s, t))

min_T_go = dijkstra(X, graph_reverse)           # 각 마을에서 X로 "도착"하는 최소 시간 리스트
min_T_back = dijkstra(X, graph)                 # X에서 각 마을로 "출발"하는 최소 시간 리스트
ans = 0
for i in range(1, N+1):
    T = min_T_go[i] + min_T_back[i]             # 둘을 더하면 오고 가는 시간
    if T > ans:
        ans = T
print(ans)


# 최적화안된거
# def dijkstra(start, end):
#     global min_T_back
#
#     inf = float('INF')
#     min_T = [inf] * (N+1)
#     min_T[start] = 0
#     news = [(0, start)]
#
#     while news:                                 # 다익스트라로 최소 시간 길 찾기
#         T, now = heapq.heappop(news)
#         if min_T[now] >= T:
#             for new_village, t in graph[now]:
#                 new_T = min_T[now] + t
#                 if new_T < min_T[new_village]:
#                     min_T[new_village] = new_T
#                     heapq.heappush(news, (new_T, new_village))
#
#     if start == end:                            # 시작지점이 도착지점이면, 그 외 지점으로 가는 최소 시간을 구함
#         min_T_back = min_T
#
#     return min_T[end]                           # 도착지점까지 최소 시간 반환
#
#
# N, M, X = map(int, sys.stdin.readline().rstrip().split())
# graph = [[] for _ in range(N+1)]
# for _ in range(M):
#     s, e, t = map(int, sys.stdin.readline().rstrip().split())
#     graph[s].append((e, t))
#
# min_T_go = [0] * (N+1)                          # 각 학생마다 도착지점까지 걸리는 최소 시간 저장
# min_T_back = 0                                  # 도착지점에서 각 마을까지 걸리는 최소 시간 저장
# for start in range(1, N+1):
#     T = dijkstra(start, X)
#     min_T_go[start] = T
#
# ans = 0
# for i in range(1, N+1):                         # 각 마을에서 도착지점까지 + 도착지점부터 각 마을까지
#     if min_T_go[i] + min_T_back[i] > ans:       # 가장 큰 값을 출력
#         ans = min_T_go[i] + min_T_back[i]
# print(ans)