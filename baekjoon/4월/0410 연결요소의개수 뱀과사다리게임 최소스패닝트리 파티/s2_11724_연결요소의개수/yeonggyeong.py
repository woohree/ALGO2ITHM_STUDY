from collections import deque
import sys
sys.stdin = open('G.txt')


def bfs(x):
    # 연결된 간선이 없다면 바로 return
    if not graph[x]:
        return 

    queue = deque()
    queue.append(x)
    visited[x] = 1

    while queue:
        number = queue.popleft()

        for j in graph[number]:
            if not visited[j]:
                queue.append(j)
                visited[j] = 1
        



N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        cnt += 1
        bfs(i)

print(cnt)