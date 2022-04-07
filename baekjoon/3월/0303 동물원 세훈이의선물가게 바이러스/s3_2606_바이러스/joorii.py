import sys
sys.stdin = open('M.txt')


def worm_virus(idx):
    # 다음에 가야할 노드 리스트
    nexts = [idx]
    count = 0

    # DFS
    while nexts:
        current = nexts.pop()
        if not virus[current]:
            # 방문할 수 있는 노드는 감염되었다고 표시
            virus[current] = True
            nexts += computers[current]

    # 1을 제외한 노드부터 끝까지 바이러스에 감염된 노드 개수 카운트
    for i in range(2, len(virus)):
        if virus[i]:
            count += 1

    return count


# 컴퓨터(node)의 수 ( 1 ~ 100 )
N = int(input())

# 연결된 컴퓨터 쌍(edge)의 수
E = int(input())

computers = [[] for _ in range(N + 1)]
virus = [False for _ in range(N + 1)]

for _ in range(E):
    start, end = map(int, input().split())
    # 양쪽으로 이어질 수 있게 두 번 넣었음
    # 1 3 / 2 3
    computers[start].append(end)
    computers[end].append(start)

print(worm_virus(1))

