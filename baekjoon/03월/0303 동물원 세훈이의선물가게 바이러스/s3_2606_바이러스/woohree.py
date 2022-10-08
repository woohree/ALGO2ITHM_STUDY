import sys
sys.stdin = open('L.txt')

# 25분
# 딱 dfs 복습하기 좋은 문제!


def get_number_of_zombie_computer_DFS():
    # 1번 컴퓨터와 연결된 컴퓨터가 없을 경우, 0을 반환
    if not network[1]:
        return 0

    cnt = 0  # 감염된 컴퓨터 수
    next_v = [1]  # 1번부터 시작된 바이러스
    visited = [False]*(V+1)  # 방문도장
    while next_v:  # 다음 방문할 지점이 있다면 반복
        now = next_v.pop()  # dfs는 처음을 pop!
        if not visited[now]:
            visited[now] = True
            next_v += network[now]
            cnt += 1
    # 1번은 카운트할 필요가 없음 -1
    return cnt-1


def get_number_of_zombie_computer_BFS():
    # 1번 컴퓨터와 연결된 컴퓨터가 없을 경우, 0을 반환
    if not network[1]:
        return 0

    cnt = 0  # 감염된 컴퓨터 수
    next_v = [1]  # 1번부터 시작된 바이러스
    visited = [False]*(V+1)  # 방문도장
    while next_v:  # 다음 방문할 지점이 있다면 반복
        now = next_v.pop(0)  # bfs는 처음을 pop!
        if not visited[now]:
            visited[now] = True
            next_v += network[now]
            cnt += 1
    # 1번은 카운트할 필요가 없음 -1
    return cnt-1


def get_number_of_zombie_computer_recursive(v):
    global visited, cnt
    if not network[1]:
        return 0
    # 얘는 1번을 카운트하지 않음!
    visited[v] = True
    for new in network[v]:
        if not visited[new]:
            cnt += 1
            get_number_of_zombie_computer_recursive(new)


V = int(input())
E = int(input())
network = [[] for _ in range(V+1)]
for _ in range(E):
    s, e = map(int, input().split())
    network[s].append(e)
    network[e].append(s)
# ans = get_number_of_zombie_computer_DFS()
# ans = get_number_of_zombie_computer_BFS()
# print(ans)
visited, cnt = [False]*(V+1), 0
get_number_of_zombie_computer_recursive(1)
print(cnt)
