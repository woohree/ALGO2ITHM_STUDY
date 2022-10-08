import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('M.txt')


def connected_component(idx):
    if not visited[idx]:
        visited[idx] = 1
        for nxt in graph[idx]:
            connected_component(nxt)
    else:
        return 0
    return 1


# 정점의 개수 N, 간선의 개수 M
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

# 방문한 곳 체크
visited = [0 for _ in range(N + 1)]
cnt = 0
for i in range(1, N + 1):
    cnt += connected_component(i)
print(cnt)
