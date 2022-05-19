import sys
sys.stdin = open('M.txt')


def find_set(x, arr):
    if x != graph[x]:
        arr.append(x)
        graph[x] = find_set(graph[x], arr)
    return graph[x]


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    graph = [0 for _ in range(N + 1)]
    for _ in range(N - 1):
        p, c = map(int, sys.stdin.readline().split())
        graph[c] = p

    ta, tb = map(int, sys.stdin.readline().split())
    arr_a, arr_b = [], []
    find_set(ta, arr_a)     # ta의 부모 노드 리스트를 차례대로 구함
    find_set(tb, arr_b)     # tb의 부모 노드 리스트를 차례대로 구함 (ta와의 공통 조상까지)

    print(arr_b[-1])
