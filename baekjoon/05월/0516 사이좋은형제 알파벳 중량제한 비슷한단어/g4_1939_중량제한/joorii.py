import sys
sys.stdin = open('M.txt')


def find_set(x):
    if x != nodes[x]:
        nodes[x] = find_set(nodes[x])
    return nodes[x]


def union(a, b):
    a, b = find_set(a), find_set(b)
    nodes[max(a, b)] = min(a, b)


N, M = map(int, sys.stdin.readline().split())
graphs = []
nodes = [i for i in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graphs.append((a, b, c))
plant_a, plant_b = map(int, sys.stdin.readline().split())

graphs.sort(key=lambda x: -x[2])        # 중량제한 기준 내림차순

for graph in graphs:
    a, b, c = graph
    union(a, b)
    if find_set(plant_a) == find_set(plant_b):
        print(c)
        break
