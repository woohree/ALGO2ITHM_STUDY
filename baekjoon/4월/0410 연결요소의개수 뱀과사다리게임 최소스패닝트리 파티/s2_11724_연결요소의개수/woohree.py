import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('L.txt')


def dfs(n):
    visited[n] = 1

    for v in graph[n]:
        if not visited[v]:
            dfs(v)


N, M = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    graph[temp[0]].append(temp[1])
    graph[temp[1]].append(temp[0])

ans = 0
visited = [0] * (N+1)
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        ans += 1
print(ans)