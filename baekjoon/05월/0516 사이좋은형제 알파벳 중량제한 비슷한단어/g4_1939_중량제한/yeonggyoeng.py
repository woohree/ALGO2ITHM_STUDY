import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('G.txt')


def find_set(x):
    if x == parents[x]:
        return x
    else:
        parents[x] = find_set(parents[x])
        return parents[x]


def union(a, b):
    a = find_set(a)
    b = find_set(b)

    if a != b:
        parents[b] = a


N, M = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]
graph.sort(key=lambda x: x[-1], reverse=True)
start, end = map(int, sys.stdin.readline().split())

parents = [i for i in range(N+1)]
for g in graph:
    s, e, c = g
    # start, end 합치기
    union(s, e)
    # 시작 지점이랑 도착지점이 이어져 있다면 멈추기
    if find_set(start) == find_set(end):
        print(c)
        break