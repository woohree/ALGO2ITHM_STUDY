import sys
sys.stdin = open('G.txt')


def find_parents(node):
    node_parents = {node}
    while True:
        node = graph[node]
        if node:
            node_parents.add(node)
        else:
            return node_parents


T = int(sys.stdin.readline())

for tc in range(T):
    N = int(sys.stdin.readline())

    graph = [0 for _ in range(N+1)]

    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        # b의 부모가 누구인지 저장
        graph[b] = a

    A, B = map(int, input().split())
    # A의 조상들 다 찾기
    a_parents = find_parents(A)
    # B의 조상들 찾아가면서 동시에 A랑 겹치는지 확인하지
    b_parents, node = {B}, B
    while True:
        if set(a_parents) & b_parents:
            print(list(set(a_parents) & b_parents)[0])
            break
        node = graph[node]
        b_parents.add(node)