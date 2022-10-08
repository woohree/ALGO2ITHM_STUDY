import heapq
import sys
sys.stdin = open('M.txt')


def dijkstra():
    while hq_from_party:        # 파티 마을에서 돌아오는 다익스트라
        time, cur = heapq.heappop(hq_from_party)
        if time > dist_from_party[cur]:
            continue
        for temp_e, temp_t in graph_rev[cur]:
            new_t = time + temp_t
            if new_t < dist_from_party[temp_e]:
                dist_from_party[temp_e] = new_t
                heapq.heappush(hq_from_party, (new_t, temp_e))

    while hq_to_party:          # 각 마을에서 파티 마을까지 가는 역-다익스트라
        time, cur = heapq.heappop(hq_to_party)
        if time > dist_to_party[cur]:
            continue
        for temp_e, temp_t in graph[cur]:
            new_t = time + temp_t
            if new_t < dist_to_party[temp_e]:
                dist_to_party[temp_e] = new_t
                heapq.heappush(hq_to_party, (new_t, temp_e))


# 학생의 수 N, 도로의 수 M, 파티 마을 X
N, M, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]
graph_rev = [[] for _ in range(N)]
for _ in range(M):
    s, e, t = map(int, sys.stdin.readline().split())
    graph[s - 1].append([e - 1, t])     # [도착 마을, 소요 시간]
    graph_rev[e - 1].append([s - 1, t]) # [시작 마을, 소요 시간]

INF = float('inf')
dist_to_party = [INF for _ in range(N)]
dist_from_party = [INF for _ in range(N)]
dist_to_party[X - 1] = 0
dist_from_party[X - 1] = 0
hq_to_party, hq_from_party = [],[]
heapq.heappush(hq_from_party, (0, X - 1))   # (소요 시간, 출발 마을)
heapq.heappush(hq_to_party, (0, X - 1))     # (소요 시간, 출발 마을)
dijkstra()
print(max(dist_to_party[i] + dist_from_party[i] for i in range(N)))
