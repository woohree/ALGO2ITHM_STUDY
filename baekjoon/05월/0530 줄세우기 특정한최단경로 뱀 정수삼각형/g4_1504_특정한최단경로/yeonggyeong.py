import heapq, sys
sys.stdin = open('G.txt')

# 1 -> v1 -> v2 -> N
# 1 -> v2 -> v1 -> N 
# 중에 최단 거리 찾기 

def dijkstra(start):
    distance = [float('inf') for _ in range(N+1)]
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

N, E = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N+1)]


for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

visited1, visited2 = map(int, sys.stdin.readline().rstrip().split())

# 계산 값 저장해두기
start_1 = dijkstra(1)
start_v1 = dijkstra(visited1)
start_v2 = dijkstra(visited2)
answer = min(start_1[visited1] + start_v1[visited2] + start_v2[N], start_1[visited2] + start_v2[visited1] + start_v1[N])
print(answer if str(answer) != 'inf' else -1)


## 플로이드-와샬

# for _ in range(E):
#     s, e, c = map(int, sys.stdin.readline().rstrip().split())
#     graph[s][e] = min(graph[s][e], c)
#     graph[e][s] = min(graph[e][s], c)

# visited1, visited2 = map(int, sys.stdin.readline().rstrip().split())

# for k in range(1, N+1):
#   for start in range(1, N+1):
#     for end in range(1, N+1):
#         if start == end:
#             graph[start][end] = 0
#         graph[start][end]=min(graph[start][end], graph[start][k]+graph[k][end])

# result= min(graph[1][visited1]+graph[visited1][visited2]+graph[visited2][N], graph[1][visited2]+graph[visited2][visited1]+graph[visited1][N])
# print(result if result != 'inf' else -1)