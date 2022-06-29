import sys
sys.stdin = open('M.txt')


def find_set(x):
    if x != graph[x]:
        graph[x] = find_set(graph[x])
    return graph[x]


def union(x, y):
    graph[find_set(y)] = find_set(x)


def kruskal():
    costs = []      # 유지비용 저장 리스트
    for edge in edges:
        s, e, w = edge
        if find_set(s) != find_set(e):
            union(s, e)
            costs.append(w)

    return sum(costs[:-1])


# 집의 개수 N, 길의 개수 M
N, M = map(int, sys.stdin.readline().split())
edges = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(M)], key=lambda x: x[2])
graph = [i for i in range(N + 1)]
print(kruskal())
