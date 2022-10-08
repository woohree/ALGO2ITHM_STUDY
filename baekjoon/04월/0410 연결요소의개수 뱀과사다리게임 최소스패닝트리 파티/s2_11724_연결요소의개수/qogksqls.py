import sys
sys.stdin = open('B.txt')

# 30m
# N이 최대 1000개라돌 for 문 리는 list 로 품
# 사실상 if 조건문 달아서 품

# 1. 간선 정보 중 앞에 노드 값을 비교
# 2. 해당 노드에 값이 없으면 대표자를 정해서 저장하고 간선 정보 중 뒤에 노드 값 비교
# 3. 뒤에 노드 값이 없으면 대표자 넣어주고, 값이 있다면 for 문 돌려서 그 값과 같은 다른 노드들 값들도 대표자로 바꿔줌
# 4. 간선 정보 중 앞에 노드 값이 있다면 위에 과정 반복

N, M = map(int, sys.stdin.readline().rstrip().split())
edges = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]
nodes = [0] * (N+1)  # 노드 정보 담을 list

for edge in edges:
    # 간선 정보(전자)에 있는 노드가 값이 안 정해져 있을 경우
    if nodes[edge[0]] == 0:
        nodes[edge[0]] = edge[0]
        # 간선 정보(후자)에 있는 노드 값이 안 정해져 있을 경우
        if nodes[edge[1]] == 0:
            nodes[edge[1]] = nodes[edge[0]]
        # 노드에 값이 존재할 경우
        else:
            # 전자에 있던 노드 값과 다를 경우만 비교해서 싹다 같은 경우로 고쳐줌
            if nodes[edge[1]] != nodes[edge[0]]:
                temp = nodes[edge[1]]
                for i in range(N+1):
                    if temp == nodes[i]:
                        nodes[i] = nodes[edge[0]]
    # 노드에 값이 존재할 경우
    else:
        # 간선 정보(후자)에 있는 노드 값이 안 정해져 있을 경우
        if nodes[edge[1]] == 0:
            nodes[edge[1]] = nodes[edge[0]]
        # 노드에 값이 존재할 경우
        else:
            # 전자에 있던 노드 값과 다를 경우만 비교해서 싹다 같은 경우로 고쳐줌
            if nodes[edge[1]] != nodes[edge[0]]:
                temp = nodes[edge[1]]
                for i in range(N+1):
                    if temp == nodes[i]:
                        nodes[i] = nodes[edge[0]]

solo = 0
for i in range(1, N+1):
    if nodes[i] == 0:
        solo += 1
print(solo + len(set(nodes)) - 1)
