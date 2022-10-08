import sys
sys.stdin = open('B.txt')

'''
1. edges 라는 딕셔너리. key = 자식, value = 부모 번호이다.
2. a, b 각각의 부모 list 만들고 while 문 돌려서 부모 찾아 넣음
3. 두 list에서 첫번째로 만나는 부모 번호 찾아서 print
'''

def find_parents(n, arr):
    arr.append(n)
    while 1:
        if edges.get(arr[-1]):
            arr.append(edges[arr[-1]])
        else:
            return


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    # 1.
    edges = {}
    for i in range(N-1):
        P, C = map(int, sys.stdin.readline().rstrip().split())
        edges[C] = P

    a, b = map(int, sys.stdin.readline().rstrip().split())

    # 2.
    parents_a, parents_b = [], []
    find_parents(a, parents_a)
    find_parents(b, parents_b)

    # 3.
    flag = 0
    for p in parents_a:
        for q in parents_b:
            if p == q:
                flag = 1
                print(p)
                break
        if flag:
            break

