import heapq


# 20분
def dijkstra(n, s, graph):
    inf = float('inf')
    D = [inf] * (n+1)
    news = [(0, s)]
    D[s] = 0

    while news:
        cost, now = heapq.heappop(news)
        if cost <= D[now]:
            for new, c in graph[now]:
                new_cost = D[now] + c
                if new_cost < D[new]:
                    D[new] = new_cost
                    heapq.heappush(news, (new_cost, new))
    return D


def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    for fare in fares:                      # 경로 그리기
        start, end, weight = fare
        graph[start].append((end, weight))
        graph[end].append((start, weight))
    
    # 다익스트라 총 3번 돌림
    muzi = dijkstra(n, a, graph)            # 각 지점에서 무지까지 도달하는 최소비용 리스트
    apeach = dijkstra(n, b, graph)          # 각 지점에서 어피치까지 도달하는 최소비용 리스트
    start = dijkstra(n, s, graph)           # 시작지점에서 각 지점까지 가는 최소비용 리스트

    answer = float('inf')                   # 합석해서 가다가 무지랑 어피지 나누어서 가는 최소 비용 구하기
    for i in range(1, n+1):
        temp = muzi[i] + apeach[i] + start[i]
        if temp < answer:
            answer = temp

    return answer

n=6
s=4
a=6
b=2
fares=[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))