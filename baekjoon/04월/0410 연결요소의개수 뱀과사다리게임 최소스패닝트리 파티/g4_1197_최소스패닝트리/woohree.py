import sys
sys.stdin = open('L.txt')


def find_set(a):
    if a != rep[a]:                     # 대표값과 키값이 다르면,
        rep[a] = find_set(rep[a])       # 키의 대표값의 대표값으로 바꿔주기
    return rep[a]


def union(a, b):                        # 대표값 합치기
    rep[find_set(b)] = find_set(a)


def kruskal():
    edges.sort()                        # 가중치 기준으로 오름차순 정렬
    cnt = sum_w = 0
    for c, a, b in edges:
        if find_set(a) != find_set(b):  # 대표값이 다른 경우에만,
            cnt += 1                    # mst 요소 수 +1
            sum_w += c                  # 총 가중치 갱신
            union(a, b)                 # 대표값 합치기
            if cnt == V-1:              # mst 요소 수가 정점-1(완전신장트리 조건)라면, 
                return sum_w            # 총 가중치 반환


V, E = map(int, sys.stdin.readline().rstrip().split())
edges = []
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges.append((c, a, b))

rep = [i for i in range(V+1)]
ans = kruskal()
print(ans)