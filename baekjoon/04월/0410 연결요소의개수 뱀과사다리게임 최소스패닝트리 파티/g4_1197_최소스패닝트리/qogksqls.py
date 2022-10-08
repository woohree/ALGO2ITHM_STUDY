import sys
sys.stdin = open('B.txt')


# 대표자 찾기
def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]


# 통합
def union(x, y):
    p[y] = x


def kruskal():
    # 가중치 기준으로 오름차순 정렬
    edges.sort(key=lambda x: x[2])
    answer = 0
    for n1, n2, w in edges:
        n1 = find(n1)
        n2 = find(n2)
        # 부모노드가 안겹칠 경우만 비교
        if n1 != n2:
            union(n1, n2)
            answer += w
    return answer


V, E = map(int, sys.stdin.readline().rstrip().split())
edges = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(E)]
# 부모 노드 리스트
p = list(range(V + 1))

print(kruskal())
