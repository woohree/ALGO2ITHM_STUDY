import heapq
n, s, a, b, fares = 6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]



def solution(n, s, a, b, fares):

    def dijkstra(start, end):
        visited = [float('inf') for _ in range(n+1)]
        visited[start] = 0
        heap = []
        heapq.heappush(heap, (0, start))

        while heap:
            cost, node = heapq.heappop(heap)

            for new in graph[node]:
                new_cost = cost + new[1]
                new_node = new[0]

                if new_cost < visited[new_node]:
                    visited[new_node] = new_cost
                    heapq.heappush(heap, (new_cost, new_node))

        return visited[end]

    graph = [[] for i in range(n+1)]

    for fare in fares:
        start, end, dist = fare
        graph[start].append((end, dist))
        graph[end].append((start, dist))
    
    min_cost = dijkstra(s, a) + dijkstra(s, b)
    for i in range(1, n+1):
        if s != i:
            min_cost = min(min_cost, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))
    return min_cost

print(solution(n, s, a, b, fares))
