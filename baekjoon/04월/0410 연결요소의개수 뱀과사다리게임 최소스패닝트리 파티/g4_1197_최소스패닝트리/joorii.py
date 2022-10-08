import sys
sys.stdin = open('M.txt')


def find_set(x):
    if x != graph[x]:
        graph[x] = find_set(graph[x])
    return graph[x]


def union(x, y):
    graph[find_set(y)] = find_set(x)


def kruskal():
    temp = cnt = 0
    for edge in edges:
        s, e = edge[0], edge[1]
        if find_set(s) != find_set(e):
            temp += 1
            cnt += edge[2]
            union(s, e)
        if temp == V - 1:
            return cnt


# 정점의 개수 V, 간선의 개수 E
V, E = map(int, sys.stdin.readline().split())
edges = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(E)], key=lambda x: x[2])
graph = [i for i in range(V + 1)]
print(kruskal())
