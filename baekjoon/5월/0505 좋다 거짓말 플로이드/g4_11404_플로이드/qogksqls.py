import sys, heapq
sys.stdin = open('B.txt')
INF = int(1e9)

'''floyd_warshall 600ms
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

dist = [[INF] * n for _ in range(n)]
for i in range(m):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    dist[x-1][y-1] = min(dist[x-1][y-1], z)  # 이거 그냥 z로 했다가 틀림

for i in range(n):
    dist[i][i] = 0
    for s in range(n):
        for e in range(n):
            dist[s][e] = min(dist[s][i] + dist[i][e], dist[s][e])

for d in dist:
    for j in range(n):
        if d[j] == INF:
            d[j] = 0
    print(*d)
'''

'''다익스트라, 4000ms
roads = [[] for _ in range(n)]
for i in range(m):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    roads[x-1].append((y-1, z))
    
    
def dijkstra(start):
    distances[start] = 0
    min_queue = []
    min_queue.append((distances[start], start))
    while min_queue:
        distance = min_queue[0][0]
        current = min_queue[0][1]
        heapq.heappop(min_queue)
        if distances[current] < distance:
            continue
        for j in range(len(roads[current])):
            next_city = roads[current][j][0]
            next_distance = roads[current][j][1] + distance
            if next_distance < distances[next_city]:
                distances[next_city] = next_distance
                heapq.heappush(min_queue, (next_distance, next_city))


for s in range(n):
    distances = [INF] * n
    dijkstra(s)
    for d in range(n):
        if distances[d] == INF:
            distances[d] = 0
    print(*distances)
'''