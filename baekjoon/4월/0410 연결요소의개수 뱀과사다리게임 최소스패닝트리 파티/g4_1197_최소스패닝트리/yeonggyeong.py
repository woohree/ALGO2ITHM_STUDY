# 프림 ->> 732 크루스칼 ->> 4460
import sys, heapq
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('G.txt')

def find_set(x):
    if x == connected[x]:
        return x
    else:
        return find_set(connected[x])

def union(a,b):
    a = find_set(a)
    b = find_set(b)
    # 번호가 큰 노드가 번호가 작은 노드의 부모를 가르켜야함
    if b < a:
        connected[a] = b
    else:
        connected[b] = a

V, E = map(int, sys.stdin.readline().split())

edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])

# 자기 자신이 대표
connected = [i for i in range(V+1)]

mst = 0
for edge in edges:
    if find_set(edge[0]) != find_set(edge[1]):
        union(edge[0], edge[1])
        mst += edge[2]
print(mst)

V, E = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]
queue = []
for _ in range(E):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start].append([weight, end])
    graph[end].append([weight, start])

mst = 0
edges = 0
# 처음 시작 가중치, node
queue.append([0, 1])

while queue:
    if edges == V:
        break

    w, n = heapq.heappop(queue)
    if not visited[n]:
        visited[n] = 1
        mst += w
        edges += 1
        for i in graph[n]:
            heapq.heappush(queue, i)

print(mst)