import heapq
import sys
sys.stdin = open('G.txt')

def dijkstra(start):
    visited = [float('inf') for _ in range(N+1)]
    queue = []
    # 거리가 짧은 순서대로 push
    heapq.heappush(queue, (0, start))
    # 자기 마을까지의 거리는 0
    visited[start] = 0

    while queue:
        cost, node = heapq.heappop(queue)

        for new in graph[node]:
            new_cost = cost + new[1]
            new_node = new[0]
            # 마을까지의 거리가 가장 짧다면
            if new_cost < visited[new_node]:
                visited[new_node] = new_cost
                heapq.heappush(queue, (new_cost, new_node))
    # 파티를 진행한 마을에서 집으로 돌아오기 위한 리스트 리턴
    if start == x:
        return visited

    return visited[x]

N, M, x = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))

# 왕복 거리를 구할 리스트 
roads = [0 for _ in range(N+1)]
# 집에 돌아오는 최소 거리
back = dijkstra(x)
for i in range(1, N+1):
    if i != x:
        roads[i] = dijkstra(i)
        roads[i] += back[i]

print(max(roads))