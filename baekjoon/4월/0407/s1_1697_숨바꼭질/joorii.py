from collections import deque
import sys
sys.stdin = open('M.txt')


def hide_and_seek():
    nexts = deque()
    # [위치 인덱스, 이동횟수]
    nexts.append([N, 0])

    while 1:
        cur = nexts.popleft()
        if cur[0] == K:             # 종료조건, 동생을 찾았을 때
            return cur[1]

        if 0 <= cur[0] - 1 < 100001 and not visited[cur[0] - 1]:
            nexts.append([cur[0] - 1, cur[1] + 1])
            visited[cur[0] - 1] = True
        if 0 <= cur[0] + 1 < 100001 and not visited[cur[0] + 1]:
            nexts.append([cur[0] + 1, cur[1] + 1])
            visited[cur[0] + 1] = True
        if 0 <= cur[0] * 2 < 100001 and not visited[cur[0] * 2]:
            nexts.append([cur[0] * 2, cur[1] + 1])
            visited[cur[0] * 2] = True


N, K = map(int, input().split())
visited = [False for _ in range(100001)]
print(hide_and_seek())
