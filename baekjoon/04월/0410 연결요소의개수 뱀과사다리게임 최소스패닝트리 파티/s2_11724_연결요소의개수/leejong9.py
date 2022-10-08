import sys
input = sys.stdin.readline #이걸 추가하니까 됐다
sys.setrecursionlimit(10000)


def run(n):
    visited[n] = 1
    for i in graph[n]: #모든 간선에 대해 run을 실행해본다
        if visited[i] == 0:
            run(i)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
nums = 0

for _ in range(M):
    u, v = map(int, input().split()) #간선의 양 끝 u v를 받고
    graph[u] += [v] # 각각에 더해준다
    graph[v] += [u]

for j in range(1, N + 1):
    if visited[j] == 0:
        run(j) #연결된 부분을 돌려본다
        nums += 1

print(nums)