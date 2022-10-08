import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(1000000000)

# 가장 먼 노드를 찾는 것
def DFS(node, distance):
    global max_dist
    global check
    global max_node

    # 갈 수 있는 노드를 모두 계산
    for j in range(len(Tree[node])):
        # 아직 안 가본 노드라면
        if check[Tree[node][j][0]] == 0:
            # 가봤다고 체크
            check[Tree[node][j][0]] = 1
            # 그 노드로 이동, 이동한 거리를 추가함
            DFS(Tree[node][j][0], distance+Tree[node][j][1])
    # 갈 수 있는 노드가 없다면 누적 거리를 계산하고 최댓값이면 바꾼 후 리턴
    if distance > max_dist:
        max_dist = distance
        max_node = node
    return

N = int(input())
#양방향 트리를 저장
Tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    A, B, Dist = map(int, input().split())
    Tree[A].append([B, Dist])
    Tree[B].append([A, Dist])

# 제일 먼 거리
max_dist = 0
# 제일 먼 노드
max_node = 0

# 최상위 노드(원의 중심)에서 제일 먼 노드를 정함
check = [0]*(N+1)
check[1] = 1
DFS(1, 0)

# 제일 먼 노드에서 제일 먼 노드까지의 거리(지름)를 구함
check = [0]*(N+1)
check[max_node] = 1
DFS(max_node, 0)

print(max_dist)