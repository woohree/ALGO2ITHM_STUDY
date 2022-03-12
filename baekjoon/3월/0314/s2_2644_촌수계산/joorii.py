import sys
sys.stdin = open('M.txt')


def dfs(current):
    visited[current] = True
    distance[current] += 1

    for next in graph[current]:
        if not visited[next]:
            distance[next] = distance[current]
            dfs(next)


T = int(input())

for tc in range(T):
    # 전체 사람의 수
    n = int(input())
    # 촌수를 계산해야 하는 서로 다른 두 사람의 번호
    a, b = map(int, input().split())
    # 부모 자식들 간의 관계의 개수
    m = int(input())
    # 부모 자식간의 관계
    relatives = [list(map(int, input().split())) for _ in range(m)]

    # 양방향 그래프를 저장할 리스트
    graph = [[] for _ in range(n + 1)]

    for relative in relatives:
        graph[relative[0]].append(relative[1])
        graph[relative[1]].append(relative[0])

    # 방문한 노드를 표시할 리스트
    visited = [False for _ in range(n + 1)]

    # 시작점부터의 거리를 저장할 리스트
    distance = [-1 for _ in range(n + 1)]

    dfs(a)
    print(distance[b])
