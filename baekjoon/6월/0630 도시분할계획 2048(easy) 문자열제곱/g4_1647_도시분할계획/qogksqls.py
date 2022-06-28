import sys
sys.stdin = open('B.txt')
'''
질문 창에 "대부분 MST에서 마지막 최대 간선 수치 하나를 제외한 나머지 값을 더한 결과가 답"이라는 글을 보고 풀이
또한 프림보다 크루스칼이 더 빠르다고 그러길래 크루스칼로 풀이
이걸 어케 첨부터 MST로 풀지?
'''

V, E = map(int, sys.stdin.readline().rstrip().split())
edges = []
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().rstrip().split())
    edges.append((C, A, B))
edges.sort()
p = list(range(V+1))


def find(x):
    if x == p[x]:
        return x
    p[x] = find(p[x])
    return p[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if b < a:
        p[a] = b
    else:
        p[b] = a


ans = []
for w, s, e in edges:
    if find(s) != find(e):
        union(s, e)
        ans.append(w)
ans.pop()  # 가장 큰 값 pop
print(sum(ans))
