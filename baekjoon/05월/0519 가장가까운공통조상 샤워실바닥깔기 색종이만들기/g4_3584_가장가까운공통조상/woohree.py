import sys
sys.stdin = open('L.txt')


T = int(sys.stdin.readline())
for tc in range(T):
    N = int(sys.stdin.readline())
    tree = [0] * (N+1)
    for _ in range(N-1):
        p, c = map(int, sys.stdin.readline().split())
        tree[c] = p                         # 자식노드에 부모노드 저장
    a, b = map(int, sys.stdin.readline().split())

    a_parents, b_parents = [0, a], [0, b]   # 0 없으면 인덱스 에러, 자기 자신이 공통 조상인 경우
    while tree[a] != 0 or tree[b] != 0:     # 조상 노드 싹 구해서 리스트에 저장
        if tree[a] != 0:
            a_parents.append(tree[a])
            a = tree[a]
        if tree[b] != 0:
            b_parents.append(tree[b])
            b = tree[b]

    i = -1
    while a_parents[i] == b_parents[i]:     # 뒤에서부터, 다른 조상이 나오는 순간 탈출!
        i -= 1
        
    print(a_parents[i+1])
