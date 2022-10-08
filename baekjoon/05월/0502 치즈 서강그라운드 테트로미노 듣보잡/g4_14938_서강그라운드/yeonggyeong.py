import sys, heapq
sys.stdin = open('G.txt')


def dijkstra(start):
    visited = [float('inf') for _ in range(n+1)]

    heap = []
    heapq.heappush(heap, (0, start))
    visited[start] = 0

    while heap:
        cost, node = heapq.heappop(heap)

        for new in graph[node]:
            new_cost = cost + new[1]
            new_node = new[0]

            if new_cost < visited[new_node]:
                visited[new_node] = new_cost
                heapq.heappush(heap, (new_cost, new_node))

    return visited


n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]

items = list(map(int, input().split()))

for _ in range(r):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))
    graph[end].append((start, weight))

answer = []
for i in range(1, n+1):
    visited = dijkstra(i)
    item = items[i-1]
    for j in range(1, n+1):
        if i != j and visited[j] <= m:
            item += items[j-1]
    answer.append(item)
print(max(answer))