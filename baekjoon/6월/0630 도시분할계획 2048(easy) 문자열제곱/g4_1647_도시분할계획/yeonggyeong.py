import sys
sys.stdin = open('G.txt')


def find(x):
    if connected[x] != x:
        connected[x] = find(connected[x])
    return connected[x]


def union(a,b):
    a = find(a)
    b = find(b)

    if b < a:
        connected[a] = b
    else:
        connected[b] = a


N, M = map(int, sys.stdin.readline().split())

edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[2])

connected = [i for i in range(N+1)]

mst = []
for edge in edges:
    if find(edge[0]) != find(edge[1]):
        union(edge[0], edge[1])
        mst.append(edge[2])
print(sum(mst[:-1]))
