import sys
sys.stdin = open('L.txt')


def count_distance(v):
    global cnt, signal
    visited[v] = True
    if v == b:                                  # a에서 시작해서 b에 도착했다면,
        signal = True                           # 촌수 관계가 존재!
        print(cnt)                              # 촌수를 출력
    cnt += 1                                    # 위로든 아래로든 이동한다면 cnt += 1
    for to_visit in graph[v]:                   # 그 외, b를 찾아 헤맨다.
        if not visited[to_visit]:
            count_distance(to_visit)
    cnt -= 1                                    # 위아래로 탐색을 마쳤다면 원상복구!


n = int(sys.stdin.readline().rstrip())
a, b = map(int, sys.stdin.readline().rstrip().split())
m = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0
signal = False
for _ in range(m):
    parent, child = map(int, sys.stdin.readline().rstrip().split())
    graph[child].append(parent)
    graph[parent].append(child)
count_distance(a)
if not signal:                                  # 촌수 관계가 존재하지 않는다면,
    print(-1)                                   # -1 출력
