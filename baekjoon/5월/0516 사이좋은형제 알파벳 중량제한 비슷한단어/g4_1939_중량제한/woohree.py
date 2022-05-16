import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('L.txt')


def dfs(v, W):                      # W 이상 무게에서 A->B 경로가 있는지 확인
    visited[v] = 1

    if v == B:
        return True

    for nxt, nxt_w in graph[v]:
        if nxt_w >= W and not visited[nxt]:
            if dfs(nxt, W):
                return True

    return False


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, sys.stdin.readline().split())
    graph[s].append((e, w))
    graph[e].append((s, w))
A, B = map(int, sys.stdin.readline().split())

l, r = 1, 1000000000                # 최대 무게 범위 안에서 최대 무게를 찾기 위한 이진탐색
while l <= r:
    mid = (l+r) // 2                # 검사할 무게
    visited = [0] * (N+1)

    if dfs(A, mid):                 # 경로가 있다면,
        l = mid + 1                 # 더 큰 무게에서 확인
    else:                           # 없으면,
        r = mid - 1                 # 줄여서 확인

print(r)                            # r 값이 최대 무게가 됨(l은 마지막에 한번 더 바뀜)