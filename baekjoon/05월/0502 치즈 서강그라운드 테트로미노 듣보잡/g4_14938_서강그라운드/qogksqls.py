import sys, heapq
sys.stdin = open('B.txt')
INF = int(1e9)

n, m, r = map(int, sys.stdin.readline().rstrip().split())
items = list(map(int, sys.stdin.readline().rstrip().split()))

roads = [[] for _ in range(n)]
for i in range(r):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    roads[x - 1].append((y - 1, z))
    roads[y - 1].append((x - 1, z))


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
        for k in range(len(roads[current])):
            next_ = roads[current][k][0]
            next_distance = roads[current][k][1] + distance
            if next_distance < distances[next_]:
                distances[next_] = next_distance
                heapq.heappush(min_queue, (next_distance, next_))


my_max = 0
for s in range(n):
    distances = [INF] * n
    dijkstra(s)
    count = items[s]
    for j in range(n):
        # 시작 지점이 아니고 수색 범위 내일 경우
        if distances[j] != 0 and distances[j] <= m:
            count += items[j]
    my_max = max(my_max, count)
print(my_max)
