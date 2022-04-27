import heapq


def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n)]
    for fare in fares:
        graph[fare[0] - 1].append([fare[1] - 1, fare[2]])
        graph[fare[1] - 1].append([fare[0] - 1, fare[2]])

        INF = float('inf')
        dist = [[INF for _ in range(n)] for _ in range(3)]
        dist[0][s - 1], dist[1][a - 1], dist[2][b - 1] = 0, 0, 0    # dist[0] = 출발지점 시작, dist[1] = a 도착지점 시작, dist[2] = b 도착지점 시작

    def dijkstra(idx, start):
        hq = []
        heapq.heappush(hq, (0, start))

        while hq:
            cost, cur = heapq.heappop(hq)
            if dist[idx][cur] < cost:
                continue
            for temp_u, temp_c in graph[cur]:
                new_c = temp_c + cost
                if new_c < dist[idx][temp_u]:
                    dist[idx][temp_u] = new_c
                    heapq.heappush(hq, (new_c, temp_u))

    dijkstra(0, s - 1)
    dijkstra(1, a - 1)
    dijkstra(2, b - 1)

    answer = min(sum(nums) for nums in list(zip(dist[0], dist[1], dist[2])))

    return answer


n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))
