import sys, heapq
sys.stdin = open('B.txt')


def dijkstra(village, graph, x):
    graph[x-1] = 0
    queue = []
    heapq.heappush(queue, (graph[x-1], graph.index(graph[x-1])))

    while queue:
        vertex, index = heapq.heappop(queue)
        if graph[index] < vertex:
            continue
        else:
            for e, w in village[index+1].items():
                weight = w + vertex
                if graph[e-1] >= weight:
                    graph[e-1] = weight
                    heapq.heappush(queue, (graph[e-1], e-1))


INF = sys.maxsize
N, M, X = map(int, sys.stdin.readline().rstrip().split())
village = {}
rev_village = {}
roads = [INF for _ in range(N)]
reverse_roads = [INF for _ in range(N)]
for i in range(1, N+1):
    village[i] = {}
    rev_village[i] = {}
for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())
    village[u][v] = w
    rev_village[v][u] = w

dijkstra(village, roads, X)
dijkstra(rev_village, reverse_roads, X)

my_max = 0
for i in range(len(roads)):
    my_max = max(my_max, roads[i] + reverse_roads[i])
print(my_max)

'''
# dfs로 풀이
def go_home_dfs(x, t):
    global min_go_home

    if min_go_home <= t:
        return

    if x == student:
        min_go_home = min(min_go_home, t)
        return
    for road in roads:
        if x == road[0] and visited[x] == 0:
            visited[x] = 1
            go_home_dfs(road[1], t + road[2])
            visited[x] = 0


def go_x_dfs(s, t):
    global min_go_x

    if min_go_x <= t:
        return

    if s == X:
        min_go_x = min(min_go_x, t)
        return
    for road in roads:
        if s == road[0] and visited[s] == 0:
            visited[s] = 1
            go_x_dfs(road[1], t + road[2])
            visited[s] = 0


N, M, X = map(int, sys.stdin.readline().rstrip().split())  # 학생 수(마을 개수), 단방향 도로 개수, 찾아 갈 마을 번호
roads = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]  # 시작점, 끝점, 소요시간
    
my_max = 0
for student in range(1, N+1):
    # X번 마을 찾아가기
    visited = [0] * (N+1)
    min_go_x = 99999999999
    go_x_dfs(student, 0)

    # 집가기
    visited = [0] * (N+1)
    min_go_home = 99999999999
    go_home_dfs(X, 0)

    # 학생 별 최단거리 중 가장 오래 걸리는 학생 구하기
    temp = min_go_x + min_go_home
    my_max = max(my_max, temp)

print(my_max)
'''