import sys
sys.stdin = open('L.txt')


def find_set(a):
    if a != rep[a]:
        rep[a] = find_set(rep[a])
    return rep[a]


def union(a, b):
    rep[find_set(b)] = find_set(a)


def kruskal():
    edges.sort()
    cnt = sum_w = 0
    for c, a, b in edges:
        if find_set(a) != find_set(b):
            cnt += 1
            sum_w += c
            union(a, b)
            if cnt == V-2:              # 정점 다 돌면(V-1) 전체가 다 이어진 거니까,
                return sum_w            # V-2개 됐을 때 끝내면, 마을 2개로 분할임


V, E = map(int, sys.stdin.readline().rstrip().split())
edges = []
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges.append((c, a, b))

rep = [i for i in range(V+1)]
ans = kruskal()
print(ans)