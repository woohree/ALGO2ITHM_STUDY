import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('W.txt')


def dfs(s, w):
    global max_n
    if dist[s] > dist[max_n]:           # 노드 찾기
        max_n = s

    for new, weight in tree[s]:
        if dist[new] == -1:             # 방문 안한 노드라면,
            dist[new] = w + weight      # 그 노드까지의 거리 갱신
            dfs(new, dist[new])


n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c, w = map(int, sys.stdin.readline().rstrip().split())
    tree[p].append((c, w))
    tree[c].append((p, w))

max_n = 0
dist = [-1] * (n+1)
dist[1] = 0
dfs(1, 0)                               # 1번 노드에서 가장 가중치가 큰 노드 찾기

dist = [-1] * (n+1)
dist[max_n] = 0
dfs(max_n, 0)                           # 앞에서 구한 노드부터 가장 가중치가 큰 노드 찾기
print(dist[max_n])                      # 두 노드 사이의 거리가 트리의 지름